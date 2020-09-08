from django.shortcuts import render
from rest_framework import viewsets

import coin_catalog.models as CoinModel
import coin_catalog.api.serializers as CoinSerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Region.objects.all()
    serializer_class = CoinSerializer.RegionSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Country.objects.all()
    serializer_class = CoinSerializer.CountrySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Category.objects.all()
    serializer_class = CoinSerializer.CategorySerialier


class CollectionViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Collection.objects.all()
    serializer_class = CoinSerializer.CollectionSerializer


class MintedByViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.MintedBy.objects.all()
    serializer_class = CoinSerializer.MintedBySerializer


class AuthorNameViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.AuthorName.objects.all()
    serializer_class = CoinSerializer.AuthorNameSerializer


class SculptorNameViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.SculptorName.objects.all()
    serializer_class = CoinSerializer.SculptorNameSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Material.objects.all()
    serializer_class = CoinSerializer.MaterialSerializer


class QualityViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Quality.objects.all()
    serializer_class = CoinSerializer.QualitySerializer


class EdgeViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Edge.objects.all()
    serializer_class = CoinSerializer.EdgeSerializer


class ShapeViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Shape.objects.all()
    serializer_class = CoinSerializer.ShapeSerializer


class CoinFamilyViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.CoinFamily.objects.all()
    serializer_class = CoinSerializer.CoinFamilySerializer


class CoinStyleViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.CoinStyle.objects.all()
    serializer_class = CoinSerializer.CoinStyleSerializer


class SubStyleViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.SubStyle.objects.all()
    serializer_class = CoinSerializer.SubStyleSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Note.objects.all()
    serializer_class = CoinSerializer.NoteSerializer


class SideOfCoinViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.SideOfCoin.objects.all()
    serializer_class = CoinSerializer.SideOfCoinSerializer


class CoinAuthorViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.CoinAuthor.objects.all()
    serializer_class = CoinSerializer.CoinAuthorSerializer


class CoinSculptorViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.CoinSculptor.objects.all()
    serializer_class = CoinSerializer.CoinSculptorSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset         = CoinModel.Image.objects.all()
    serializer_class = CoinSerializer.ImageSerializer
