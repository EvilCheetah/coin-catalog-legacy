from rest_framework import serializers

import coin_catalog.models as CoinModel


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.Region
        fields     = ['id', 'name']
        validators = []


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.Country
        fields     = ['id', 'region', 'name']
        validators = []


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.Category
        fields     = ['id', 'country', 'name']
        validators = []


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.Collection
        fields     = ['id', 'category', 'name']
        validators = []


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.Currency
        fields     = ['id', 'name']
        validators = []


class CountryCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.CountryCurrency
        fields     = ['id', 'country', 'currency']
        validators = []


class MintedBySerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.MintedBy
        fields     = ['id', 'name']
        validators = []


class DesignerNameSerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.DesignerName
        fields     = ['id', 'name']
        validators = []


class SculptorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.SculptorName
        fields     = ['id', 'name']
        validators = []


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.Material
        fields     = ['id', 'name']
        validators = []


class QualitySerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.Quality
        fields     = ['id', 'name']
        validators = []


class EdgeSerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.Edge
        fields     = ['id', 'name']
        validators = []


class ShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.Shape
        fields     = ['id', 'name']
        validators = []


class CoinFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.CoinFamily
        fields     = ['id', 'collection', 'name']
        validators = []


class CoinStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.CoinStyle
        fields     = ['id', 'coin_family', 'additional_name',
                      'minted_by', 'year',
                      'denomination_value', 'denomination_currency',
                      'shape', 'quality', 'edge',
                      'material', 'standard', 'mintage',
                      'km_number', 'is_substyle',
                      'weight', 'length', 'width', 'thickness',
                      'date_created', 'last_edited']
        validators = []


class SubStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.SubStyle
        fields     = ['substyle_coin', 'parent_coin']
        validators = []
        # Removes the check for One-To-One Field in CREATE Method
        extra_kwargs = {
            "substyle_coin": {
                "validators": [],
            },
        }


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.Note
        fields     = ['id', 'coin_style', 'description']
        validators = []


class SideOfCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.SideOfCoin
        fields     = ['id', 'name']
        validators = []


class CoinAllDesignersSerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.CoinDesigner
        fields     = ['id', 'coin_style', 'side', 'designer']
        validators = []


class CoinAllSculptorsSerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.CoinSculptor
        fields     = ['id', 'coin_style', 'side', 'sculptor']
        validators = []


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model      = CoinModel.Image
        fields     = ['id', 'coin_style', 'side', 'image']
        validators = []
