from django.urls import path

from .views import WeatherHomeView

from .views import index
app_name = 'weather'
urlpatterns = [
    path('index/', index, name='weather-index'),
    path('', WeatherHomeView.as_view(), name='weather-home'),
]