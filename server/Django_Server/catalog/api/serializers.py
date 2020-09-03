from rest_framework import serializers

from catalog.models import (
    CoinStyle,
    SubStyle,
    Note,
    CoinAuthor,
    CoinSculptor,
    Image
)


class CoinSerializer(serializers.ModelSerializer):
    # region      = serializers.SerializerMethodField()
    # country     = serializers.SerializerMethodField()
    # category    = serializers.SerializerMethodField()
    # collection  = serializers.SerializerMethodField()
    # coin_name   = serializers.SerializerMethodField()
    # minted_by   = serializers.SerializerMethodField()
    # shape       = serializers.SerializerMethodField()
    # quality     = serializers.SerializerMethodField()
    # edge        = serializers.SerializerMethodField()
    # material    = serializers.SerializerMethodField()
    # substyle_of = serializers.SerializerMethodField()
    #note        = serializers.SerializerMethodField()
    # authors     = serializers.SerializerMethodField()
    # sculptors   = serializers.SerializerMethodField()
    # images      = serializers.SerializerMethodField()

    class Meta:
        model  = CoinStyle
        fields = '__all__'
    #
    # def get_region(self, coin_style):
    #     return coin_style.coin.collection.category.country.region.name
    #
    # def get_country(self, coin_style):
    #     return coin_style.coin.collection.category.country.name
    #
    # def get_category(self, coin_style):
    #     return coin_style.coin.collection.category.name
    #
    # def get_collection(self, coin_style):
    #     return coin_style.coin.collection.name
    #
    # def get_coin_name(self, coin_style):
    #     return coin_style.coin.name
    #
    # def get_minted_by(self, coin_style):
    #     return coin_style.coin.minted_by.name
    #
    # def get_shape(self, coin_style):
    #     return coin_style.shape.name
    #
    # def get_quality(self, coin_style):
    #     return coin_style.quality.name
    #
    # def get_edge(self, coin_style):
    #     return coin_style.edge.name
    #
    # def get_material(self, coin_style):
    #     return coin_style.material.name
    #
    # ## TODO: search SubStyleConnector for coin_style.pk in substyle column
    # ##       return parent id
    # def get_substyle_of(self, coin_style):
    #     return None
