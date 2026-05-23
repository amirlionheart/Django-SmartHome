from django.urls import path
from .views import SensorListCreateView, SensorDetailView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view()),
    path('sensors/<int:pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
]