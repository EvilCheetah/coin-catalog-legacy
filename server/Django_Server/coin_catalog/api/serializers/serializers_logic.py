import coin_catalog.models as CoinModel


def _is_list(object):
    return isinstance(object, list)


def _convert_to_list(object):
    return object if _is_list(object) else [object]


def get_number_of_coins_from_region(region_id):
    return get_number_of_coins_from_country(
        [country.id for country in CoinModel.Country.objects.filter(region_id = region_id)]
    )


def get_number_of_coins_from_country(country_id_list):
    country_id_list = _convert_to_list(country_id_list)

    return get_number_of_coins_from_categoty(
        [category.id for category in CoinModel.Category.objects.filter(country_id__in = country_id_list)]
    )


def get_number_of_coins_from_categoty(category_id_list):
    category_id_list = _convert_to_list(category_id_list)

    return get_number_of_coins_from_collection(
        [collection.id for collection in CoinModel.Collection.objects.filter(category_id__in = category_id_list)]
    )


def get_number_of_coins_from_collection(collection_id_list):
    collection_id_list = _convert_to_list(collection_id_list)

    return get_number_of_coins_from_coin_family(
        [coin_family.id for coin_family in CoinModel.CoinFamily.objects.filter(collection_id__in = collection_id_list)]
    )


def get_number_of_coins_from_coin_family(coin_family_id_list):
    coin_family_id_list = _convert_to_list(coin_family_id_list)

    return CoinModel.CoinStyle.objects.filter(coin_family_id__in = coin_family_id_list).count()
