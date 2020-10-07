from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

import coin_catalog.models as CoinModel
import coin_catalog.api.serializers.list_serializers as CoinListSerializer
import coin_catalog.api.serializers.instance_serializers as CoinInstanceSerializer
import coin_catalog.api.filters as CoinFilter
import coin_catalog.api.view_logic as ViewSetLogic


class RegionViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Region.objects.all()
    serializer_class = CoinListSerializer.RegionSerializer
    filterset_class  = CoinFilter.RegionFilter

    def get_queryset(self):
        return ViewSetLogic.get_region_queryset(self.request)

    def retrieve(self, request, pk = None):
        return Response(ViewSetLogic._get_object_instance(
                                primary_key = pk,
                                model_      = CoinModel.Region,
                                serializer_ = CoinInstanceSerializer.RegionSerializer,
                                request     = self.request))


class CountryViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Country.objects.all()
    serializer_class = CoinListSerializer.CountrySerializer

    def get_queryset(self):
        return ViewSetLogic.get_country_queryset(self.request)

    def retrieve(self, request, pk = None):
        return Response(ViewSetLogic._get_object_instance(
                                primary_key = pk,
                                model_      = CoinModel.Country,
                                serializer_ = CoinInstanceSerializer.CountrySerializer,
                                request     = self.request))


class CategoryViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Category.objects.all()
    serializer_class = CoinListSerializer.CategorySerialier
    filterset_class  = CoinFilter.CategoryFilter

    def get_queryset(self):
        return ViewSetLogic.get_category_queryset(self.request)

    def retrieve(self, request, pk = None):
        return Response(ViewSetLogic._get_object_instance(
                                primary_key = pk,
                                model_      = CoinModel.Category,
                                serializer_ = CoinInstanceSerializer.CategorySerializer,
                                request     = self.request))


class CollectionViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Collection.objects.all()
    serializer_class = CoinListSerializer.CollectionSerializer
    filterset_class  = CoinFilter.CollectionFilter

    def get_queryset(self):
        return ViewSetLogic.get_collection_queryset(self.request)

    def retrieve(self, request, pk = None):
        return Response(ViewSetLogic._get_object_instance(
                                primary_key = pk,
                                model_      = CoinModel.Collection,
                                serializer_ = CoinInstanceSerializer.CollectionSerializer,
                                request     = self.request))

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Currency.objects.all()
    serializer_class = CoinListSerializer.CurrencySerializer


class MintedByViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.MintedBy.objects.all()
    serializer_class = CoinListSerializer.MintedBySerializer


class AuthorNameViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.AuthorName.objects.all()
    serializer_class = CoinListSerializer.AuthorNameSerializer


class SculptorNameViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.SculptorName.objects.all()
    serializer_class = CoinListSerializer.SculptorNameSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Material.objects.all()
    serializer_class = CoinListSerializer.MaterialSerializer


class QualityViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Quality.objects.all()
    serializer_class = CoinListSerializer.QualitySerializer


class EdgeViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Edge.objects.all()
    serializer_class = CoinListSerializer.EdgeSerializer


class ShapeViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Shape.objects.all()
    serializer_class = CoinListSerializer.ShapeSerializer


class CoinFamilyViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.CoinFamily.objects.all()
    serializer_class = CoinListSerializer.CoinFamilySerializer

    def get_queryset(self):
        return ViewSetLogic.get_coin_family_queryset(self.request)

    def retrieve(self, request, pk = None):
        return Response(ViewSetLogic._get_object_instance(
                                primary_key = pk,
                                model_      = CoinModel.CoinFamily,
                                serializer_ = CoinInstanceSerializer.CoinFamilySerializer,
                                request     = self.request))


class CoinStyleViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.CoinStyle.objects.all()
    serializer_class = CoinListSerializer.CoinStyleSerializer

    def get_queryset(self):
        return ViewSetLogic.get_coin_style_queryset(self.request)

    def retrieve(self, request, pk = None):
        queryset = CoinModel.CoinStyle.objects.filter(pk = pk)
        serializer = CoinInstanceSerializer.CoinStyleSerializer(queryset, many = True, context = {'request': self.request})
        return Response(serializer.data)


class SubStyleViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.SubStyle.objects.all()
    serializer_class = CoinListSerializer.SubStyleSerializer

    def get_queryset(self):
        return ViewSetLogic.get_sub_style_queryset(self.request)


class NoteViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Note.objects.all()
    serializer_class = CoinListSerializer.NoteSerializer


class SideOfCoinViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.SideOfCoin.objects.all()
    serializer_class = CoinListSerializer.SideOfCoinSerializer


class CoinAuthorViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.CoinAuthor.objects.all()
    serializer_class = CoinListSerializer.CoinAllAuthorsSerializer


class CoinSculptorViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.CoinSculptor.objects.all()
    serializer_class = CoinListSerializer.CoinAllSculptorsSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Image.objects.all()
    serializer_class = CoinListSerializer.ImageSerializer
