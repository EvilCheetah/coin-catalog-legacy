import coin_catalog.models as CoinModel


##-------------------Local Functions-------------------##
"""
These functions are used only here
"""
def _is_list(object):
    return isinstance(object, list)


def _convert_to_list(object):
    return object if _is_list(object) else [object]


##-------------------Get Number of Coins-------------------##
"""
These functions get the total number of coins
"""
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


##-------------------Get Region Functions-------------------##
"""
These functions get region name
"""
def get_region_from_country(country_object):
    return country_object.region.name

def get_region_from_category(category_object):
    return get_region_from_country(category_object.country)

def get_region_from_collection(collection_object):
    return get_region_from_category(collection_object.category)

def get_region_from_coin_family(coin_family_object):
    return get_region_from_collection(coin_family_object.collection)

def get_region_from_coin_style(coin_style_object):
    return get_region_from_coin_family(coin_style_object.coin_family)


##-------------------Get Country Functions-------------------##
def get_country_from_category(category_object):
    return category_object.country.name

def get_country_from_collection(collection_object):
    return get_country_from_category(collection_object.category)

def get_country_from_coin_family(coin_family_object):
    return get_country_from_collection(coin_family_object.collection)

def get_country_from_coin_style(coin_style_object):
    return get_country_from_coin_family(coin_style_object.coin_family)


##-------------------Get Category Functions-------------------##
#def get
