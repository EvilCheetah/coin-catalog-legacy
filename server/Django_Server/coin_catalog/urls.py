from django.urls import path, include
from rest_framework import routers
from coin_catalog.api.views import CoinViewSet


urlpatterns = [
    path('', include('coin_catalog.api.urls')),
]
