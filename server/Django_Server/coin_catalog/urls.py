from django.urls import path, include
from rest_framework import routers


urlpatterns = [
    path('', include('coin_catalog.api.urls')),
]
