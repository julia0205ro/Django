from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from measurement.views import SensorUpdate, SensorCreateView, MeasurementCreate

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('v1/sensors/', SensorCreateView.as_view()),
    path('v1/sensors/<int:pk>/', SensorUpdate.as_view()),
    path('v1/measurements/', MeasurementCreate.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
