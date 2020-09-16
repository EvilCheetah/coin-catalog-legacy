from rest_framework import serializers

import coin_catalog.models as CoinModel
import coin_catalog.api.serializers.serializers_logic as Logic


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    total_coins = serializers.SerializerMethodField('get_number_of_coins')

    class Meta:
        model = CoinModel.Region
        fields = ['id', 'name', 'total_coins']

    def get_number_of_coins(self, region):
        return Logic.get_number_of_coins_from_region(region.id)


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    region      = serializers.SerializerMethodField('get_region_name')
    total_coins = serializers.SerializerMethodField('get_number_of_coins')

    class Meta:
        model  = CoinModel.Country
        fields = ['id', 'region', 'name', 'total_coins']

    def get_region_name(self, country):
        return Logic.get_region_from_country(country)

    def get_number_of_coins(self, country):
        return Logic.get_number_of_coins_from_country(country.id)


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    region      = serializers.SerializerMethodField('get_region_name')
    country     = serializers.SerializerMethodField('get_country_name')
    total_coins = serializers.SerializerMethodField('get_number_of_coins')

    class Meta:
        model  = CoinModel.Category
        fields = ['id', 'region', 'country', 'name', 'total_coins']

    def get_region_name(self, category):
        return Logic.get_region_from_category(category)

    def get_country_name(self, category):
        return Logic.get_country_from_category(category)

    def get_number_of_coins(self, category):
        return Logic.get_number_of_coins_from_categoty(category.id)


class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    region      = serializers.SerializerMethodField('get_region_name')
    country     = serializers.SerializerMethodField('get_country_name')
    total_coins = serializers.SerializerMethodField('get_number_of_coins')

    class Meta:
        model  = CoinModel.Collection
        fields = ['id', 'region', 'country', 'category', 'name', 'total_coins']

    def get_region_name(self, collection):
        return Logic.get_region_from_collection(collection)

    def get_country_name(self, collection):
        return Logic.get_country_from_collection(collection)

    def get_number_of_coins(self, collection):
        return Logic.get_number_of_coins_from_collection(collection.id)


class MintedBySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = CoinModel.MintedBy
        fields = ['id', 'name']


class AuthorNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = CoinModel.AuthorName
        fields = ['id', 'name']


class SculptorNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = CoinModel.SculptorName
        fields = ['id', 'name']


class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = CoinModel.Material
        fields = ['id', 'name']


class QualitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = CoinModel.Quality
        fields = ['id', 'name']


class EdgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = CoinModel.Edge
        fields = ['id', 'name']


class ShapeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = CoinModel.Shape
        fields = ['id', 'name']


class CoinFamilySerializer(serializers.HyperlinkedModelSerializer):
    region      = serializers.SerializerMethodField('get_region_name')
    country     = serializers.SerializerMethodField('get_country_name')
    #authors     = serializers.SerializerMethodField()
    #sculptors   = serializers.SerializerMethodField()
    total_coins = serializers.SerializerMethodField('get_number_of_coins')

    class Meta:
        model  = CoinModel.CoinFamily
        fields = ['id', 'region', 'country', 'collection', 'name', 'minted_by', 'total_coins']

    # def get_authors(self, object):
    #     author_list = (CoinModel.CoinAuthor).objects.filter(coin_family = object.pk)
    #     return CoinAuthorSerializer(author_list, many = True, context = self.context).data
    #
    # def get_sculptors(self, object):
    #     sculptor_list = (CoinModel.CoinSculptor).objects.filter(coin_family = object.pk)
    #     return CoinSculptorSerializer(sculptor_list, many = True, context = self.context).data

    def get_region_name(self, coin_family):
        return Logic.get_region_from_coin_family(coin_family)

    def get_country_name(self, coin_family):
        return Logic.get_country_from_coin_family(coin_family)

    def get_number_of_coins(self, coin_family):
        return Logic.get_number_of_coins_from_coin_family(coin_family.id)


class CoinStyleSerializer(serializers.HyperlinkedModelSerializer):
    region      = serializers.SerializerMethodField('get_region_name')
    country     = serializers.SerializerMethodField('get_country_name')
    coin_name = serializers.SerializerMethodField()
    shape     = serializers.SerializerMethodField()
    quality   = serializers.SerializerMethodField()
    edge      = serializers.SerializerMethodField()
    material  = serializers.SerializerMethodField()
    dimentions = serializers.SerializerMethodField()
    weight    = serializers.SerializerMethodField()
    # authors   = serializers.SerializerMethodField()
    # sculptors = serializers.SerializerMethodField()

    class Meta:
        model  = CoinModel.CoinStyle
        fields = ['id',  'region', 'country',
                  'year',     'coin_name',
                  'additional_name',
                  'shape',     'quality',  'edge',
                  'material',  'standard', 'denomination',
                  'mintage',   'weight',   'dimentions',
                  'km_number', 'is_rare',  'is_substyle',
                  ]

    def get_region_name(self, coin_style):
        return Logic.get_region_from_coin_style(coin_style)

    def get_country_name(self, coin_style):
        return Logic.get_country_from_coin_style(coin_style)

    def get_coin_name(self, coin_style_object):
        return coin_style_object.coin_family.name

    def get_shape(self, coin_style_object):
        return coin_style_object.shape.name

    def get_quality(self, coin_style_object):
        return coin_style_object.quality.name

    def get_edge(self, coin_style_object):
        return coin_style_object.edge.name

    def get_material(self, coin_style_object):
        return coin_style_object.material.name

    def get_dimentions(self, coin_style_object):
        if (coin_style_object.shape.name == "Round"):
            return ("Ø " + str(coin_style_object.length) + " mm")

        else:
            return ( str(coin_style_object.length) + " x " + str(coin_style_object.width) + " mm" )

    def get_weight(self, coin_style_object):
        return ( str(coin_style_object.weight) + ' g')
    #
    # def get_authors(self, coin_style_object):
    #     return 0
    #
    # def get_sculptors(self, coin_style_object):
    #     return 0

class SubStyleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = CoinModel.SubStyle
        fields = ['substyle_coin', 'parent_coin']


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = CoinModel.Note
        fields = ['id', 'coin_style', 'description']


class SideOfCoinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = CoinModel.SideOfCoin
        fields = ['id', 'name']


class CoinAuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = CoinModel.CoinAuthor
        fields = ['author', 'side']


class CoinAllAuthorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = CoinModel.CoinAuthor
        fields = ['id', 'coin_family', 'author', 'side']


class CoinSculptorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = CoinModel.CoinSculptor
        fields = ['sculptor', 'side']


class CoinAllSculptorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = CoinModel.CoinSculptor
        fields = ['id', 'coin_family', 'sculptor', 'side']


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = CoinModel.Image
        fields = ['id', 'coin_style', 'side', 'path']
