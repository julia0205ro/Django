from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=256, blank=True)

    objects = models.Manager()


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    measurement_temp = models.DecimalField(max_digits=3, decimal_places=1)
    measurement_datetime = models.DateTimeField(auto_now=True)

    objects = models.Manager()
