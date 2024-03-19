from django.urls import path

from .views import get_all_view, get_destinations_view, travel_options_view

urlpatterns = [
  path('', get_all_view, name="list"),
  path('destinations', get_destinations_view, name="destinations"),
  path('options', travel_options_view, name="travel_options"),
]