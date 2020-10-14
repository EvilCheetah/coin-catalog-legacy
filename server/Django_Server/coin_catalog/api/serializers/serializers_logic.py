import coin_catalog.models as CoinModel
from coin_catalog.api.serializers import list_serializers as CoinListSerializer

##-------------------Local Functions-------------------##
def _is_list(object):
    return isinstance(object, list)


def _convert_to_list(object):
    return object if _is_list(object) else [object]


##-------------------Get Number of Coins-------------------##
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
def get_category_from_collection(collection_object):
    return collection_object.category.name

def get_category_from_coin_family(coin_family_object):
    return get_category_from_collection(coin_family_object.collection)

def get_category_from_coin_style(coin_style_object):
    return get_category_from_coin_family(coin_style_object.coin_family)


##-------------------Get Collection Functions-------------------##
def get_collection_from_coin_family(coin_family_object):
    return coin_family_object.collection.name


def get_collection_from_coin_style(coin_style_object):
    return get_collection_from_coin_family(coin_style_object.coin_family)


##-------------------Get Coin Family Function-------------------##
def get_coin_family_from_coin_style(coin_style_object):
    return coin_style_object.coin_family.name


##---------------Denomination-Currency Functions---------------##
def get_currency_from_coin_style(coin_style_object):
    return coin_style_object.denomination_currency.currency.name


##---------------Substyle Information Function---------------##
def get_substyle_status_from_coin_style(coin_style_object):
    coin_sub_style_object = CoinModel.SubStyle.objects.filter(substyle_coin = coin_style_object)

    if ( coin_sub_style_object ):
        return coin_sub_style_object[0].parent_coin.id

    return None


##-------------------Get Authors Functions-------------------##
def get_authors_from_coin_family(coin_family_object):
    return [
        {
            'side':   coin_author_object.side.name,
            'author': coin_author_object.author.name
        }
        for coin_author_object in
        CoinModel.CoinAuthor.objects.filter(coin_family_id = coin_family_object.id)
    ]

def get_authors_from_coin_style(coin_style_object):
    return get_authors_from_coin_family(coin_style_object.coin_family)


##-------------------Get Sculptors Functions-------------------##
def get_sculptors_from_coin_family(coin_family_object):
    return [
        {
            'side':     coin_sculptor_object.side.name,
            'sculptor': coin_sculptor_object.sculptor.name
        }

        for coin_sculptor_object in
        CoinModel.CoinSculptor.objects.filter(coin_family_id = coin_family_object.id)
    ]

def get_sculptors_from_coin_style(coin_style_object):
    return get_sculptors_from_coin_family(coin_style_object.coin_family)


def get_notes_from_coin_style(coin_style_object):
    return [
        note.description
        for note in
        CoinModel.Note.objects.filter(coin_style_id = coin_style_object.id)
    ]


def get_minted_by_from_coin_family(coin_family_object):
    return coin_family_object.minted_by.id

def get_minted_by_from_coin_style(coin_style_object):
    return get_minted_by_from_coin_family(coin_style_object.coin_family)


def get_images_from_coin_style(coin_style_object):
    return [
        {
            'side': image_object.side.name,
            'path': image_object.path
        }
        for image_object in
        CoinModel.Image.objects.filter(coin_style_id = coin_style_object.id)
    ]


def get_notes_for_preloaded_coin(coin_style_object):
    return CoinListSerializer.NoteSerializer(
                CoinModel.Note.objects.filter(coin_style_id = coin_style_object.id),
                many = True
           ).data


def get_authors_for_pre_loaded_coin(coin_style_object):
    return CoinListSerializer.CoinAllAuthorsSerializer(
                CoinModel.CoinAuthor.objects.filter(coin_family_id = coin_style_object.coin_family.id),
                many = True
           ).data


def get_sculptors_for_pre_loaded_coin(coin_style_object):
    return CoinListSerializer.CoinAllSculptorsSerializer(
                CoinModel.CoinSculptor.objects.filter(coin_family_id = coin_style_object.coin_family.id),
                many = True
           ).data


def get_images_for_pre_loaded_coin(coin_style_object):
    return CoinListSerializer.ImageSerializer(
                CoinModel.Image.objects.filter(coin_style_id = coin_style_object.id),
                many = True
           ).data
