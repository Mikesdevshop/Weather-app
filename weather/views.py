from django.shortcuts import render
from django.views.generic import TemplateView

from .models import City
from .forms import CityForm

import requests

class WeatherHomeView(TemplateView):
    template_name='weather/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=839ba7e69d5e2b0a1b31dd8a065684d5'
        cities = City.objects.all()

        weather_data = []

        for city in cities:
            city_weather = requests.get(url.format(city)).json()

            weather = {
                'city' : city,
                'temperature' : city_weather['main']['temp'],
                'description' : city_weather['weather'][0]['description'],
                'icon' : city_weather['weather'][0]['icon'],
            }

            weather_data.append(weather)

        context = {'weather_data' : weather_data}

        return context
    

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=839ba7e69d5e2b0a1b31dd8a065684d5'
    cities = City.objects.all()

    if request.method == "POST":
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon'],
        }

        weather_data.append(weather)

    context = {'weather_data' : weather_data, 'form' : form}

    return render(request,'weather/index.html', context)