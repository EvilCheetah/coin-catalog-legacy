from rest_framework import serializers

import coin_catalog.models as Coin

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Coin.Region
        fields = ['id', 'name']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Coin.Country
        fields = ['id', 'region', 'name']


class CategorySerialier(serializers.ModelSerializer):
    class Meta:
        model  = Coin.Category
        fields = ['id', 'country', 'name']


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Coin.Collection
        fields = ['id', 'category', 'name']


class MintedBySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Coin.MintedBy
        fields = ['id', 'name']


class AuthorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Coin.AuthorName
        fields = ['id', 'name']


class SculptorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Coin.SculptorName
        fields = ['id', 'name']


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Coin.Material
        fields = ['id', 'name']


class QualitySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Coin.Quality
        fields = ['id', 'name']


class EdgeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Coin.Edge
        fields = ['id', 'name']


class ShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Coin.Shape
        fields = ['id', 'name']


class CoinFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Coin.CoinFamily
        fields = ['id', 'collection', 'name', 'minted_by']


class CoinStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Coin.CoinStyle
        fields = ['id',        'year',     'coin_family',
                  'shape',     'quality',  'edge',
                  'material',  'standard', 'denomination',
                  'mintage',   'additional_name',
                  'km_number', 'is_rare',  'is_substyle',
                  'weight',    'length',   'width']


class SubStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Coin.SubStyle
        fields = ['substyle_coin', 'parent_coin']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Coin.Note
        fields = ['id', 'coin_style', 'description']


class SideOfCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Coin.SideOfCoin
        fields = ['id', 'name']


class CoinAllAuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Coin.CoinAuthor
        fields = ['id', 'coin_family', 'author', 'side']


class CoinAllSculptorsSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Coin.CoinSculptor
        fields = ['id', 'coin_family', 'sculptor', 'side']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Coin.Image
        fields = ['id', 'coin_style', 'side', 'path']
