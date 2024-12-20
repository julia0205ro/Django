from django.urls import path

from measurement.views import SensorUpdate, SensorCreateView, MeasurementCreate

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('v1/sensors/', SensorCreateView.as_view()),
    path('v1/sensors/<int:pk>/', SensorUpdate.as_view()),
    path('v1/measurements/', MeasurementCreate.as_view()),
]
