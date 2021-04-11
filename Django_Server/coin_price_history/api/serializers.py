from rest_framework import serializers

import coin_price_history.models as PriceHistoryModel
# import coin_price_history.services.serializers_logic as Logic


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model  = PriceHistoryModel.Platform
        fields = ['id', 'name']


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = PriceHistoryModel.Grade
        fields = ['id', 'name', 'abbreviation']


class CoinPriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = PriceHistoryModel.CoinPriceHistory
        fields = ['id', 'coin_style', 'platform', 'grade', 'purchase_id', 'date', 'purchase_price']

#
# class CoinStyleFormattedPriceHistory(serializers.ModelSerializer):
#     price_history = serializers.SerializerMethodField('get_price_history')
#
#     class Meta:
#         model  = PriceHistoryModel.CoinPriceHistory
#         fields = ['coin_style', 'price_history']
#
#     def get_price_history(self, coin_style_price_history_object):
#         return Logic.get_formatted_coin_history_for_individual_coin_style(coin_style_price_history_object)
