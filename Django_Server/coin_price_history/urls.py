from django.urls import path, include
from rest_framework import routers


urlpatterns = [
    path('', include('coin_price_history.api.urls')),
]
