import coin_catalog.models as CoinModel
from coin_catalog.api.serializers import list_serializers as CoinListSerializer
from coin_catalog.api.serializers import instance_serializers as CoinInstanceSerializer

##-------------------Local Functions-------------------##
def _is_list(object):
    return isinstance(object, list)


def _convert_to_list(object):
    return object if _is_list(object) else [object]


##-------------------Get Number of Coins-------------------##
"""
These Functions are designated to return the number of CoinStyle
objects that are present in the any 'parent' model, with specified
id of 'parent' model
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
These functions are designated to return 'region' name based on any
descendant object that was specified
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
"""
These functions are designated to return 'country' name based on any
descendant object that was specified
"""
def get_country_from_category(category_object):
    return category_object.country.name

def get_country_from_collection(collection_object):
    return get_country_from_category(collection_object.category)

def get_country_from_coin_family(coin_family_object):
    return get_country_from_collection(coin_family_object.collection)

def get_country_from_coin_style(coin_style_object):
    return get_country_from_coin_family(coin_style_object.coin_family)


##-------------------Get Category Functions-------------------##
"""
These functions are designated to return 'category' name based on any
descendant object that was specified
"""
def get_category_from_collection(collection_object):
    return collection_object.category.name

def get_category_from_coin_family(coin_family_object):
    return get_category_from_collection(coin_family_object.collection)

def get_category_from_coin_style(coin_style_object):
    return get_category_from_coin_family(coin_style_object.coin_family)


##-------------------Get Collection Functions-------------------##
"""
These functions are designated to return 'collection' name based on any
descendant object that was specified
"""
def get_collection_from_coin_family(coin_family_object):
    return coin_family_object.collection.name


def get_collection_from_coin_style(coin_style_object):
    return get_collection_from_coin_family(coin_style_object.coin_family)


##-------------------Get Coin Family Function-------------------##
"""
This function is designated to return 'coin_family' name based on any
descendant object that was specified
"""
def get_coin_family_from_coin_style(coin_style_object):
    return coin_style_object.coin_family.name


##---------------Denomination-Currency Functions---------------##
"""
This function is designated to return 'currency' name based on
specified coin_style object
"""
def get_currency_from_coin_style(coin_style_object):
    return coin_style_object.denomination_currency.currency.name


##---------------Substyle Information Function---------------##
"""
This function is designated to return the parent id of the 'coin_style'
    If Coin is a substyle of another coin, returns the ID of parent Coin
    else returns NULL
"""
def get_substyle_status_from_coin_style(coin_style_object):
    coin_sub_style_object = CoinModel.SubStyle.objects.filter(substyle_coin = coin_style_object)

    if ( coin_sub_style_object ):
        return coin_sub_style_object.first().parent_coin.id

    return None


##-------------------Get Authors Functions-------------------##
"""
These functions are designated to return a list of 'authors' name based on
specified object
"""
def get_designers_from_coin_style(coin_style_object):
    return [
        {
            'side': coin_designer_object.side.name,
            'name': coin_designer_object.designer.name
        }
        for coin_designer_object in
        CoinModel.CoinDesigner.objects.filter(coin_style_id = coin_style_object.id)
    ]


##-------------------Get Sculptors Functions-------------------##
"""
These functions are designated to return a list of 'sculptors' name based on
specified object
"""
def get_sculptors_from_coin_style(coin_style_object):
    return [
            {
                'side': coin_sculptor_object.side.name,
                'name': coin_sculptor_object.sculptor.name
            }

            for coin_sculptor_object in
            CoinModel.CoinSculptor.objects.filter(coin_style_id = coin_style_object.id)
        ]


def get_notes_from_coin_style(coin_style_object):
    return [
        note.description
        for note in
        CoinModel.Note.objects.filter(coin_style_id = coin_style_object.id)
    ]


##-------------------------Get Minted By-------------------------##
"""
These functions are designated to return 'minted' id based on
specified object
"""
def get_minted_by_from_coin_style(coin_style_object):
    return coin_style_object.minted_by.name


##
"""
These functions are designated to return a list of 'images' name based on
coin style object
with given format:
    side: side_name
    path: path_string
"""
def get_images_from_coin_style(coin_style_object):
    return [
        {
            'side': image_object.side.name,
            'image': image_object.image.url
        }
        for image_object in
        CoinModel.Image.objects.filter(coin_style_id = coin_style_object.id)
    ]


##-------------------Pre Loaded Information For CoinFamily-------------------##
"""
These functions are designated to obtain the required information
based on coin_family or coin_style
"""
def get_styles_for_pre_loaded_coin_family(coin_family_object):
    return CoinInstanceSerializer.CoinStyleSerializerForPreloadedCoinFamily(
                CoinModel.CoinStyle.objects.filter(coin_family_id = coin_family_object.id),
                many = True
           ).data


def get_image_queryset_from_coin_style(coin_style_object):
    return CoinInstanceSerializer.ImageSerializer(
                CoinModel.Image.objects.filter(coin_style_id = coin_style_object.id),
                many = True
           ).data


def get_notes_queryset_from_coin_style(coin_style_object):
    return CoinInstanceSerializer.NoteSerializer(
                CoinModel.Note.objects.filter(coin_style_id = coin_style_object.id),
                many = True
           ).data


##-------------------PreLoaded Information For CoinStyle-------------------##
def get_substyle_list_from_coin_style(coin_style_object):
    list_of_substyles = CoinModel.SubStyle.objects.filter(
                            parent_coin_id = coin_style_object.id
                        ).values_list('substyle_coin_id', flat = True)

    return CoinInstanceSerializer.CoinStyleSerializer(
                CoinModel.CoinStyle.objects.filter(id__in = list(list_of_substyles)),
                many = True
           ).data
