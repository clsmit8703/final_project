from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from .views import WelcomeView, FoodView

class UrlTests(TestCase):
    def test_welcome_url(self):
        welcome = resolve(reverse('foodgen:welcome'))
        return self.assertEqual(welcome.func.__name__,
                                WelcomeView.__name__)

    def test_food_url(self):
        food = resolve(reverse('foodgen:food'))
        return self.assertEqual(food.func.__name__,
                                FoodView.__name__)
