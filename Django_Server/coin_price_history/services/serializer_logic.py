from collections import defaultdict

import coin_price_history.models as PriceHistoryModel


def get_formatted_coin_history_for_individual_coin_style(coin_style_price_history_object):
    prices = defaultdict( list )

    queryset = PriceHistoryModel.CoinPriceHistory.objects.filter(coin_style_id = coin_style_price_history_object.coin_style.id)

    for platform, date, price in ( queryset.values_list('platform__name', 'date', 'price') ):
        prices[platform].append(
            {
                'date':  date,
                'price': price
            }
        )

    return prices
