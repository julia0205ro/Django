from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    # pass

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(default='')

    objects = models.Manager()
