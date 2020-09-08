from django.urls import path, include


urlpatterns = [
    path('', include('coin_catalog.api.urls')),
]
