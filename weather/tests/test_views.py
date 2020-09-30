from django.test import TestCase
from django.urls import reverse

from weather.models import City
import random

class WeatherViewTests(TestCase):

    def test_home_url(self):
        '''Test to verify the home page is accessible by URL location and name.'''
        location = self.client.get("/")
        name = self.client.get(reverse('weather:weather-home'))
        self.assertEqual(location.status_code, 200)
        self.assertEqual(name.status_code, 200)
    
    def test_home_shows_all_cities(self):
        '''Tests to verify all cities in the DB (3) are listed in the home view.'''
        pass

    def test_index_url(self):
        """Test to verify the index page is accessible by URL location and name."""
        location = self.client.get("/index/")
        name = self.client.get(reverse('weather:weather-index'))
        self.assertEqual(location.status_code, 200)
        self.assertEqual(name.status_code, 200)