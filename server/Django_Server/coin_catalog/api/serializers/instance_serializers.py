from rest_framework import serializers

import coin_catalog.models as CoinModel
import coin_catalog.api.serializers.serializers_logic as Logic


class RegionSerializer(serializers.ModelSerializer):
    total_coins  = serializers.SerializerMethodField('get_number_of_coins')
    country_list = serializers.HyperlinkedRelatedField(
        view_name    = 'country-detail',
        read_only    = True,
        many         = True)

    class Meta:
        model = CoinModel.Region
        fields = ['id', 'name', 'total_coins', 'country_list']

    def get_number_of_coins(self, region_object):
        return Logic.get_number_of_coins_from_region(region_object.id)


class CountrySerializer(serializers.ModelSerializer):
    region        = serializers.SerializerMethodField('get_region')
    total_coins   = serializers.SerializerMethodField('get_number_of_coins')
    category_list = serializers.HyperlinkedRelatedField(
        view_name = 'category-detail',
        read_only = True,
        many      = True)

    class Meta:
        model  = CoinModel.Country
        fields = ['id', 'region', 'name', 'total_coins', 'category_list']

    def get_region(self, country_object):
        return Logic.get_region_from_country(country_object)

    def get_number_of_coins(self, country_object):
        return Logic.get_number_of_coins_from_country(country_object.id)


class CategorySerializer(serializers.ModelSerializer):
    region          = serializers.SerializerMethodField('get_region_name')
    country         = serializers.SerializerMethodField('get_country_name')
    total_coins     = serializers.SerializerMethodField('get_number_of_coins')
    collection_list = serializers.HyperlinkedRelatedField(
        view_name = 'collection-detail',
        read_only = True,
        many      = True
    )

    class Meta:
        model  = CoinModel.Category
        fields = ['id', 'region', 'country', 'name', 'total_coins', 'collection_list']

    def get_region_name(self, category_object):
        return Logic.get_region_from_category(category_object)

    def get_country_name(self, category_object):
        return Logic.get_country_from_category(category_object)

    def get_number_of_coins(self, category_object):
        return Logic.get_number_of_coins_from_categoty(category_object.id)


class CollectionSerializer(serializers.ModelSerializer):
    region      = serializers.SerializerMethodField('get_region')
    country     = serializers.SerializerMethodField('get_country')
    category    = serializers.SerializerMethodField('get_category')
    total_coins = serializers.SerializerMethodField('get_number_of_coins')
    coin_family_list = serializers.HyperlinkedRelatedField(
        view_name = 'coinfamily-detail',
        read_only = True,
        many      = True
    )

    class Meta:
        model  = CoinModel.Collection
        fields = ['id', 'region', 'country', 'category', 'name', 'total_coins', 'coin_family_list']

    def get_region(self, collection_object):
        return Logic.get_region_from_collection(collection_object)

    def get_country(self, collection_object):
        return Logic.get_country_from_collection(collection_object)

    def get_category(self, collection_object):
        return Logic.get_category_from_collection(collection_object)

    def get_number_of_coins(self, collection_object):
        return Logic.get_number_of_coins_from_collection(collection_object.id)


class MintedBySerializer(serializers.ModelSerializer):
    class Meta:
        model  = CoinModel.MintedBy
        fields = ['id', 'name']


class AuthorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CoinModel.AuthorName
        fields = ['id', 'name']


class SculptorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CoinModel.SculptorName
        fields = ['id', 'name']


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CoinModel.Material
        fields = ['id', 'name']


class QualitySerializer(serializers.ModelSerializer):
    class Meta:
        model  = CoinModel.Quality
        fields = ['id', 'name']


class EdgeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CoinModel.Edge
        fields = ['id', 'name']


class ShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CoinModel.Shape
        fields = ['id', 'name']


class CoinFamilySerializer(serializers.ModelSerializer):
    region      = serializers.SerializerMethodField('get_region')
    country     = serializers.SerializerMethodField('get_country')
    category    = serializers.SerializerMethodField('get_category')
    collection  = serializers.SerializerMethodField('get_collection')
    total_coins = serializers.SerializerMethodField('get_number_of_coins')
    authors     = serializers.SerializerMethodField('get_authors')
    sculptors   = serializers.SerializerMethodField('get_sculptors')
    coin_style_list = serializers.HyperlinkedRelatedField(
        view_name = 'coinstyle-detail',
        read_only = True,
        many      = True
    )

    class Meta:
        model  = CoinModel.CoinFamily
        fields = ['id',
                  #ancestors
                  'region', 'country', 'category', 'collection',
                  'name',
                  'total_coins',
                  #creators
                  'authors', 'sculptors', 'minted_by',
                  'coin_style_list']

    def get_region(self, coin_family_object):
        return Logic.get_region_from_coin_family(coin_family_object)

    def get_country(self, coin_family_object):
        return Logic.get_country_from_coin_family(coin_family_object)

    def get_category(self, coin_family_object):
        return Logic.get_category_from_coin_family(coin_family_object)

    def get_collection(self, coin_family_object):
        return Logic.get_collection_from_coin_family(coin_family_object)

    def get_number_of_coins(self, coin_family_object):
        return Logic.get_number_of_coins_from_coin_family(coin_family_object.id)

    def get_authors(self, coin_family_object):
        return Logic.get_authors_from_coin_family(coin_family_object)

    def get_sculptors(self, coin_family_object):
        return Logic.get_sculptors_from_coin_family(coin_family_object)

    def get_minted_by(self, coin_family_object):
        return Logic.get_minted_by_from_coin_family(coin_family_object)


class CoinStyleSerializer(serializers.ModelSerializer):
    region      = serializers.SerializerMethodField('get_region')
    country     = serializers.SerializerMethodField('get_country')
    category    = serializers.SerializerMethodField('get_category')
    collection  = serializers.SerializerMethodField('get_collection')
    coin_family = serializers.SerializerMethodField('get_coin_family')
    coin_name   = serializers.SerializerMethodField('get_coin_name')
    authors     = serializers.SerializerMethodField('get_authors')
    sculptors   = serializers.SerializerMethodField('get_sculptors')
    minted_by   = serializers.SerializerMethodField('get_minted_by')
    images      = serializers.SerializerMethodField('get_images')

    class Meta:
        model  = CoinModel.CoinStyle
        fields = ['id',
                  #ancestors
                  'region', 'country', 'category', 'collection', 'coin_family',
                  #basic info
                  'year', 'coin_name', 'additional_name',
                  #coin characteristics and value
                  'shape',     'quality',  'edge',
                  'material',  'standard',
                  'denomination', 'mintage',
                  #physical properties
                  'weight',   'length', 'width', 'thickness',
                  'km_number', 'is_rare',  'is_substyle',
                  #creators
                  'authors', 'sculptors', 'minted_by', 'images'
                  ]

    def get_region(self, coin_style_object):
        return Logic.get_region_from_coin_style(coin_style_object)

    def get_country(self, coin_style_object):
        return Logic.get_country_from_coin_style(coin_style_object)

    def get_category(self, coin_style_object):
        return Logic.get_category_from_coin_style(coin_style_object)

    def get_collection(self, coin_style_object):
        return Logic.get_collection_from_coin_style(coin_style_object)

    def get_coin_family(self, coin_style_object):
        return Logic.get_coin_family_from_coin_style(coin_style_object)

    def get_coin_name(self, coin_style_object):
        return coin_style_object.coin_family.name

    def get_authors(self, coin_style_object):
        return Logic.get_authors_from_coin_style(coin_style_object)

    def get_sculptors(self, coin_style_object):
        return Logic.get_sculptors_from_coin_style(coin_style_object)

    def get_minted_by(self, coin_style_object):
        return Logic.get_minted_by_from_coin_style(coin_style_object)

    def get_images(self, coin_style_object):
        return Logic.get_images_from_coin_style(coin_style_object)


class SubStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CoinModel.SubStyle
        fields = ['substyle_coin', 'parent_coin']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CoinModel.Note
        fields = ['id', 'coin_style', 'description']


class SideOfCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CoinModel.SideOfCoin
        fields = ['id', 'name']


class CoinAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CoinModel.CoinAuthor
        fields = ['author', 'side']


class CoinAllAuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CoinModel.CoinAuthor
        fields = ['id', 'coin_family', 'author', 'side']


class CoinSculptorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CoinModel.CoinSculptor
        fields = ['sculptor', 'side']


class CoinAllSculptorsSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CoinModel.CoinSculptor
        fields = ['id', 'coin_family', 'sculptor', 'side']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CoinModel.Image
        fields = ['id', 'coin_style', 'side', 'path']
