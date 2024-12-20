from rest_framework import serializers

from measurement.models import Sensor, Measurement


# TODO: опишите необходимые сериализаторы


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor_id', 'measurement_temp', 'measurement_datetime', 'image']


class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(required=False, read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
