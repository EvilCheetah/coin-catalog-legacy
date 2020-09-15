from rest_framework import serializers

import coin_catalog.models as Coin


class RegionSerializer(serializers.ModelSerializer):
    total_coins = serializers.SerializerMethodField()

    class Meta:
        model = Coin.Region
        fields = ['id', 'name', 'total_coins']

    def get_country_number(self, region):
        return len( (Coin.Country).objects.filter(region_id = region.pk) )


class CountrySerializer(serializers.ModelSerializer):
    region_name = serializers.SerializerMethodField()
    total_coins = serializers.SerializerMethodField()

    class Meta:
        model  = Coin.Country
        fields = ['id', 'region_name', 'name', 'total_coins']

    def get_region_name(self, country):
        return country.region.name

    def get_total_coins(self, country):
        country_categories  = [x.id for x in Coin.Category.objects.filter(country_id = country.pk)]
        country_collections = [x.id for x in Coin.Collection.objects.filter(category_id__in = country_categories)]
        country_coin_families = [x.id for x in Coin.CoinFamily.objects.filter(collection_id__in = country_collections)]
        country_coin_styles = [x.id for x in Coin.CoinStyle.objects.filter(coin_family_id__in = country_coin_families)]

        return len(country_coin_styles)



class CategorySerialier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Coin.Category
        fields = ['id', 'country', 'name']


class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Coin.Collection
        fields = ['id', 'category', 'name']


class MintedBySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Coin.MintedBy
        fields = ['id', 'name']


class AuthorNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Coin.AuthorName
        fields = ['id', 'name']


class SculptorNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Coin.SculptorName
        fields = ['id', 'name']


class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Coin.Material
        fields = ['id', 'name']


class QualitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Coin.Quality
        fields = ['id', 'name']


class EdgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Coin.Edge
        fields = ['id', 'name']


class ShapeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Coin.Shape
        fields = ['id', 'name']


class CoinFamilySerializer(serializers.HyperlinkedModelSerializer):
    authors   = serializers.SerializerMethodField()
    sculptors = serializers.SerializerMethodField()

    class Meta:
        model  = Coin.CoinFamily
        fields = ['id', 'collection', 'name', 'minted_by', 'authors', 'sculptors']

    def get_authors(self, object):
        author_list = (Coin.CoinAuthor).objects.filter(coin_family = object.pk)
        return CoinAuthorSerializer(author_list, many = True, context = self.context).data

    def get_sculptors(self, object):
        sculptor_list = (Coin.CoinSculptor).objects.filter(coin_family = object.pk)
        return CoinSculptorSerializer(sculptor_list, many = True, context = self.context).data


class CoinStyleSerializer(serializers.HyperlinkedModelSerializer):
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
        model  = Coin.CoinStyle
        fields = ['id',        'year',     'coin_name',
                  'additional_name',
                  'shape',     'quality',  'edge',
                  'material',  'standard', 'denomination',
                  'mintage',   'weight',   'dimentions',
                  'km_number', 'is_rare',  'is_substyle',
                  ]

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
        model  = Coin.SubStyle
        fields = ['substyle_coin', 'parent_coin']


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Coin.Note
        fields = ['id', 'coin_style', 'description']


class SideOfCoinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Coin.SideOfCoin
        fields = ['id', 'name']


class CoinAuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Coin.CoinAuthor
        fields = ['author', 'side']


class CoinAllAuthorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Coin.CoinAuthor
        fields = ['id', 'coin_family', 'author', 'side']


class CoinSculptorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Coin.CoinSculptor
        fields = ['sculptor', 'side']


class CoinAllSculptorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Coin.CoinSculptor
        fields = ['id', 'coin_family', 'sculptor', 'side']


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Coin.Image
        fields = ['id', 'coin_style', 'side', 'path']
