from django.shortcuts import render

import requests

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=839ba7e69d5e2b0a1b31dd8a065684d5'
    city = 'Honolulu'
    city_weather = requests.get(url.format(city)).json()

    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon'],
    }
    context = {'weather' : weather}

    return render(request,'weather/index.html', context)