from rest_framework import serializers

import coin_catalog.models as CoinModel
import coin_catalog.api.serializers.serializers_logic as Logic


class RegionSerializer(serializers.ModelSerializer):
    total_coins  = serializers.SerializerMethodField('get_number_of_coins')

    class Meta:
        model = CoinModel.Region
        fields = ['id', 'name', 'total_coins',
                  #Displays the list of IDs of Country
                  #'country_list'
                 ]

    def get_number_of_coins(self, region_object):
        return Logic.get_number_of_coins_from_region(region_object.id)


class CountrySerializer(serializers.ModelSerializer):
    total_coins   = serializers.SerializerMethodField('get_number_of_coins')

    class Meta:
        model  = CoinModel.Country
        fields = ['id', 'region', 'name', 'total_coins',
                  #Displays the list of IDs of Category
                  #'category_list'
                 ]

    def get_number_of_coins(self, country_object):
        return Logic.get_number_of_coins_from_country(country_object.id)


class CategorySerializer(serializers.ModelSerializer):
    total_coins     = serializers.SerializerMethodField('get_number_of_coins')

    class Meta:
        model  = CoinModel.Category
        fields = ['id', 'country', 'name', 'total_coins',
                  #Displays the list of IDs of Collection
                  #'collection_list'
                 ]

    def get_number_of_coins(self, category_object):
        return Logic.get_number_of_coins_from_categoty(category_object.id)


class CollectionSerializer(serializers.ModelSerializer):
    total_coins = serializers.SerializerMethodField('get_number_of_coins')

    class Meta:
        model  = CoinModel.Collection
        fields = ['id', 'category', 'name', 'total_coins',
                  ##Displays the list of IDs of CoinFamily
                  #'coin_family_list'
                 ]

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
    total_coins = serializers.SerializerMethodField('get_number_of_coins')
    class Meta:

        model  = CoinModel.CoinFamily
        fields = ['id',
                  'collection',
                  'name',
                  #creators
                  #'authors', 'sculptors',
                  'minted_by',
                  'total_coins',
                  ##Displays the list of IDs of CoinStyle
                  #'coin_style_list'
                  ]

    def get_number_of_coins(self, coin_family_object):
        return Logic.get_number_of_coins_from_coin_family(coin_family_object.id)


class CoinStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CoinModel.CoinStyle
        fields = ['id',
                  #ancestors
                  ##'region', 'country', 'category', 'collection',
                  'coin_family',
                  #basic info
                  'year',
                  ##'coin_name',
                  #coin characteristics and value
                  'denomination_value',
                  'denomination_currency',
                  'shape',     'quality',  'edge',
                  'material',  'standard',
                  'mintage',

                  'additional_name',
                  #physical properties
                  'km_number', 'is_rare',  'is_substyle',
                  'weight',   'length', 'width', 'thickness',
                  #creators and additional information
                  ##'authors', 'sculptors', 'notes',
                  ##'minted_by', 'images'
                  ]


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


##-----------------------Preloaded Coin Serializers-----------------------##
class PreLoadedCoinFamilySerializer(serializers.ModelSerializer):
    authors         = serializers.SerializerMethodField('get_authors')
    sculptors       = serializers.SerializerMethodField('get_sculptors')
    styles          = serializers.SerializerMethodField('get_styles')

    class Meta:
        model  = CoinModel.CoinFamily
        fields = ['id', 'collection', 'name', 'minted_by',
                  'authors', 'sculptors', 'styles']

    def get_authors(self, coin_family_object):
        return Logic.get_authors_for_pre_loaded_coin_family(coin_family_object)

    def get_sculptors(self, coin_family_object):
        return Logic.get_sculptors_for_pre_loaded_coin_family(coin_family_object)

    def get_styles(self, coin_family_object):
        return Logic.get_styles_for_pre_loaded_coin_family(coin_family_object)


class PreLoadedCoinStyleSerializer(serializers.ModelSerializer):
    substyle_of = serializers.SerializerMethodField('get_substyle_status')
    notes       = serializers.SerializerMethodField('get_notes')
    images      = serializers.SerializerMethodField('get_images')

    class Meta:
        model  = CoinModel.CoinStyle
        fields = ['id', 'coin_family', 'year',
                  'denomination_value', 'denomination_currency',
                  'shape', 'quality', 'edge', 'material', 'standard',
                  'mintage',
                  'additional_name', 'km_number',
                  'is_rare', 'substyle_of',
                  'weight', 'length', 'width', 'thickness',
                  'notes', 'images'
                  ]

    def get_substyle_status(self, coin_style_object):
        return Logic.get_substyle_status_from_coin_style(coin_style_object)

    def get_notes(self, coin_style_object):
        return Logic.get_notes_queryset_from_coin_style(coin_style_object)

    def get_images(self, coin_style_object):
        return Logic.get_image_queryset_from_coin_style(coin_style_object)


##--------------------------Full Info Coin--------------------------##
class FullInfoCoinSerializer(serializers.ModelSerializer):
    region                = serializers.SerializerMethodField('get_region')
    country               = serializers.SerializerMethodField('get_country')
    category              = serializers.SerializerMethodField('get_category')
    collection            = serializers.SerializerMethodField('get_collection')
    coin_family           = serializers.SerializerMethodField('get_coin_family')
    #coin_name             = serializers.SerializerMethodField('get_coin_name')
    denomination_currency = serializers.SerializerMethodField('get_denomination_currency')
    shape                 = serializers.SerializerMethodField('get_shape')
    quality               = serializers.SerializerMethodField('get_quality')
    edge                  = serializers.SerializerMethodField('get_edge')
    material              = serializers.SerializerMethodField('get_material')
    substyle_of           = serializers.SerializerMethodField('get_substyle')
    authors               = serializers.SerializerMethodField('get_authors')
    sculptors             = serializers.SerializerMethodField('get_sculptors')
    notes                 = serializers.SerializerMethodField('get_notes')
    minted_by             = serializers.SerializerMethodField('get_minted_by')
    images                = serializers.SerializerMethodField('get_images')

    class Meta:
        model  = CoinModel.CoinStyle
        fields = ['id',
                  #ancestors
                  'region', 'country', 'category', 'collection', 'coin_family',
                  #basic info
                  'additional_name',
                  'year', #'coin_name',
                  #coin characteristics and value
                  'shape',     'quality',  'edge',
                  'material',  'standard',
                  'denomination_value',
                  'denomination_currency',
                  'mintage',
                  #physical properties
                  'weight',   'length', 'width', 'thickness',
                  'km_number',
                  'substyle_of',
                  ##'is_rare',  'is_substyle',
                  #creators and additional information
                  'authors', 'sculptors', 'notes',
                  'minted_by', 'images'
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

    def get_denomination_currency(self, coin_style_object):
        return Logic.get_currency_from_coin_style(coin_style_object)

    def get_shape(self, coin_style_object):
        return coin_style_object.shape.name

    def get_quality(self, coin_style_object):
        return coin_style_object.quality.name

    def get_edge(self, coin_style_object):
        return coin_style_object.edge.name

    def get_material(self, coin_style_object):
        return coin_style_object.material.name

    def get_substyle(self, coin_style_object):
        return Logic.get_substyle_status_from_coin_style(coin_style_object)

    def get_authors(self, coin_style_object):
        return Logic.get_authors_from_coin_style(coin_style_object)

    def get_sculptors(self, coin_style_object):
        return Logic.get_sculptors_from_coin_style(coin_style_object)

    def get_notes(self, coin_style_object):
        return Logic.get_notes_from_coin_style(coin_style_object)

    def get_minted_by(self, coin_style_object):
        return Logic.get_minted_by_from_coin_style(coin_style_object)

    def get_images(self, coin_style_object):
        return Logic.get_images_from_coin_style(coin_style_object)
