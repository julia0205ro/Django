import pdb

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement, FavAdvertisement
from advertisements.serializers import AdvertisementSerializer, FavAdvertisementSerializer
from api_with_restrictions.permissions import IsOwnerOrReadOnly


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        # pdb.set_trace()
        if self.action in ["create"]:
            return [IsAuthenticated()]
        elif self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return super().get_permissions()

    @action(methods=['post'], detail=True)
    def add_fav_adv(self, request, pk=None):
        """Добавление объявления в избранное."""

        title = self.get_object()
        user = request.user

        if title.creator == user:
            return Response({'status': "ad's creator cannot add their own ad to fav."},
                            status=status.HTTP_201_CREATED)

        elif FavAdvertisement.objects.filter(title=title, user=user).exists():
            return Response({'status': 'ads has been added to fav ads'},
                            status=status.HTTP_201_CREATED)
        else:
            FavAdvertisement.objects.create(title=title, user=user)
            return Response({'status': 'ads has been added to fav ads'},
                            status=status.HTTP_201_CREATED)


class FavAdvertisementViewSet(ModelViewSet):
    """ViewSet для избранных объявлений."""

    queryset = FavAdvertisement.objects.all()
    serializer_class = FavAdvertisementSerializer
