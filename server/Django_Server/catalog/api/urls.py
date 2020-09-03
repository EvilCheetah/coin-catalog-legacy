from django.urls import path
from catalog.api.views import api_coin_list

urlpatterns = [
    path('coins/', api_coin_list, name='all_regions_list')
]
