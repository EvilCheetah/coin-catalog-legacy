from django_filters import rest_framework as filters
import coin_catalog.models as CoinModel

class RegionFilter(filters.FilterSet):
    class Meta:
        model  = CoinModel.Region
        fields = {
            'name': ['icontains']
        }


class CountryFilter(filters.FilterSet):
    class Meta:
        model  = CoinModel.Country
        fields = {
            'name': ['icontains']
        }


class CategoryFilter(filters.FilterSet):
    class Meta:
        model  = CoinModel.Category
        fields = {
            'country__region__name':  ['icontains'],
            'country__name': ['icontains'],
            'name':          ['icontains']
        }


class CollectionFilter(filters.FilterSet):
    class Meta:
        model  = CoinModel.Collection
        fields = {
            'category': ['exact'],
            'name':     ['icontains']
        }
