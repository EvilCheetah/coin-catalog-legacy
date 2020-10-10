from django.db.models import Q

import coin_catalog.models as CoinModel
import coin_catalog.api.serializers.list_serializers as CoinListSerializer

CHAR_SPLIT_CHAR = ','

##----------------------Private Functions----------------------##
def _split_string(item: str) -> list:
    return item.split(CHAR_SPLIT_CHAR)


def _get_year_range_queryset(queryset, year_gte_limit, year_lte_limit):
    if ( year_gte_limit ):
        queryset = queryset.filter(year__gte = int(year_gte_limit))

    if ( year_lte_limit ):
        queryset = queryset.filter(year__lte = int(year_lte_limit))

    return queryset


def _get_standard_range_queryset(queryset, standard_gte_limit, standard_lte_limit):
    if ( standard_gte_limit ):
        queryset = queryset.filter(standard__gte = float(standard_gte_limit))

    if ( standard_lte_limit ):
        queryset = queryset.filter(standard__lte = float(standard_lte_limit))

    return queryset


def _get_denomination_queryset(queryset, denomination_value, denomination_currency):
    return queryset.filter(denomination_value = denomination_value).filter(denomination_currency__currency__id = denomination_currency)


def _get_mintage_range_queryset(queryset, mintage_gte_limit, mintage_lte_limit):
    if ( mintage_gte_limit ):
        queryset = queryset.filter(mintage__gte = int(mintage_gte_limit))

    if ( mintage_lte_limit ):
        queryset = queryset.filter(mintage__lte = int(mintage_lte_limit))

    return queryset


def _get_weight_range_queryset(queryset, weight_gte_limit, weight_lte_limit):
    if ( weight_gte_limit ):
        queryset = queryset.filter(weight__gte = float(weight_gte_limit))

    if ( weight_lte_limit ):
        queryset = queryset.filter(weight__lte = float(weight_lte_limit))

    return queryset


def _get_length_range_queryset(queryset, length_gte_limit, length_lte_limit):
    if ( length_gte_limit ):
        queryset = queryset.filter(length__gte = float(length_gte_limit))

    if ( length_lte_limit ):
        queryset = queryset.filter(length__lte = float(length_lte_limit))

    return queryset


def _get_width_range_queryset(queryset, width_gte_limit, width_lte_limit):
    if ( width_gte_limit ):
        queryset = queryset.filter(width__gte = float(width_gte_limit))

    if ( width_lte_limit ):
        queryset = queryset.filter(width__lte = float(width_lte_limit))

    return queryset


def _get_thickness_range_queryset(queryset, thickness_gte_limit, thickness_lte_limit):
    if ( thickness_gte_limit ):
        queryset = queryset.filter(thickness__gte = float(thickness_gte_limit))

    if ( thickness_lte_limit ):
        queryset = queryset.filter(thickness__lte = float(thickness_lte_limit))

    return queryset



def get_object_instance(primary_key, model_, serializer_, request):
    context = {'request': request}
    queryset = model_.objects.filter(pk = primary_key)
    serializer = serializer_(queryset, many = True, context = context)
    return serializer.data


##----------------------Queryset Functions----------------------##
def get_region_queryset(request):
    region_name = request.query_params.get('region')

    if region_name:
        return CoinModel.Region.objects.filter(name__in = _split_string(region_name))

    return CoinModel.Region.objects.all()


def get_country_queryset(request):
    queryset     = CoinModel.Country.objects.all()

    region_id    = request.query_params.get('region')
    country_name = request.query_params.get('country')

    if region_id:
        queryset = queryset.filter(region__id__in = _split_string(region_id))

    if country_name:
        queryset = queryset.filter(name__in = _split_string(country_name))

    return queryset


def get_category_queryset(request):
    queryset      = CoinModel.Category.objects.all()

    region_id     = request.query_params.get('region')
    country_id    = request.query_params.get('country')
    category_name = request.query_params.get('category')

    if region_id:
        queryset = queryset.filter(country__region__id__in = _split_string(region_id))

    if country_id:
        queryset = queryset.filter(country__id__in = _split_string(country_id))

    if category_name:
        queryset = queryset.filter(name__in = _split_string(category_name))

    return queryset


def get_collection_queryset(request):
    queryset        = CoinModel.Collection.objects.all()

    region_id       = request.query_params.get('region')
    country_id      = request.query_params.get('country')
    category_id     = request.query_params.get('category')
    collection_name = request.query_params.get('collection')

    if region_id:
        queryset = queryset.filter(category__country__region__id__in = _split_string(region_id))

    if country_id:
        queryset = queryset.filter(category__country__id__in = _split_string(country_id))

    if category_id:
        queryset = queryset.filter(category__id__in = _split_string(category_id))

    if collection_name:
        queryset = queryset.filter(name__in = _split_string(collection_name))

    return queryset


def get_coin_family_queryset(request):
    queryset = CoinModel.CoinFamily.objects.all()

    region_id        = request.query_params.get('region')
    country_id       = request.query_params.get('country')
    category_id      = request.query_params.get('category')
    collection_id    = request.query_params.get('collection')
    minted_by_id     = request.query_params.get('minted_by')

    if region_id:
        queryset = queryset.filter(collection__category__country__region__id__in = _split_string(region_id))

    if country_id:
        queryset = queryset.filter(collection__category__country__id__in = _split_string(country_id))

    if category_id:
        queryset = queryset.filter(collection__category__id__in = _split_string(category_id))

    if collection_id:
        queryset = queryset.filter(collection__id__in = _split_string(collection_id))

    if minted_by_id:
        queryset = queryset.filter(minted_by__id__in = _split_string(minted_by_id))

    return queryset


def get_coin_style_queryset(request):
    queryset = CoinModel.CoinStyle.objects.all()

    #Exact match
    km_number = request.query_params.get('km_number')

    #IF km_number is specified, return an item(usually 1 item)
    if km_number:
        return queryset.filter(km_number = km_number)

    #Ancestors parameters
    region_id             = request.query_params.get('region')
    country_id            = request.query_params.get('country')
    category_id           = request.query_params.get('category')
    collection_id         = request.query_params.get('collection')
    coin_family_id        = request.query_params.get('coin_family')
    minted_by_id          = request.query_params.get('minted_by')

    #Standard Information parameters
    year_gte_limit        = request.query_params.get('year_lte')
    year_lte_limit        = request.query_params.get('year_gte')
    shape_id              = request.query_params.get('shape')
    quality_id            = request.query_params.get('quality')
    edge_id               = request.query_params.get('edge')
    material_id           = request.query_params.get('material')
    standard_gte_limit    = request.query_params.get('standard_lte')
    standard_lte_limit    = request.query_params.get('standard_gte')
    denomination_value    = request.query_params.get('denomination_value')
    denomination_currency = request.query_params.get('denomination_currency')
    mintage_gte_limit     = request.query_params.get('mintage_gte')
    mintage_lte_limit     = request.query_params.get('mintage_lte')

    #Characteristics parameters
    weight_gte_limit      = request.query_params.get('weight_gte')
    weight_lte_limit      = request.query_params.get('weight_lte')
    length_gte_limit      = request.query_params.get('length_gte')
    length_lte_limit      = request.query_params.get('length_lte')
    width_gte_limit       = request.query_params.get('width_gte')
    width_lte_limit       = request.query_params.get('width_lte')
    thickness_gte_limit   = request.query_params.get('thickness_gte')
    thickness_lte_limit   = request.query_params.get('thickness_lte')

    #No KM - process to the filter process
    #Ancestors Search
    if region_id:
        queryset = queryset.filter(coin_family__collection__category__country__region__id__in = _split_string(region_id))
    if country_id:
        queryset = queryset.filter(coin_family__collection__category__country__id__in = _split_string(country_id))
    if category_id:
        queryset = queryset.filter(coin_family__collection__category__id__in = _split_string(category_id))
    if collection_id:
        queryset = queryset.filter(coin_family__collection__id__in = _split_string(collection_id))
    if minted_by_id:
        queryset = queryset.filter(coin_family__minted_by__id__in = _split_string(minted_by_id))

    #Standard Information Search
    if (year_gte_limit or year_lte_limit):
        queryset = _get_year_range_queryset(queryset, year_gte_limit, year_lte_limit)
    if shape_id:
        queryset = queryset.filter(shape__id__in = _split_string(shape_id))
    if quality_id:
        queryset = queryset.filter(quality__id__in = _split_string(quality_id))
    if edge_id:
        queryset = queryset.filter(edge__id__in = _split_string(edge_id))
    if material_id:
        queryset = queryset.filter(material__id__in = _split_string(material_id))
    if (standard_gte_limit or standard_gte_limit):
        queryset = _get_standard_range_queryset(queryset, standard_gte_limit, standard_lte_limit)
    #Filter IF AND ONLY IF there is Denomination Value and Currency
    if (denomination_value and denomination_currency):
        queryset = _get_denomination_queryset(queryset, denomination_value, denomination_currency)
    if (mintage_gte_limit or mintage_lte_limit):
        queryset = _get_mintage_range_queryset(queryset, mintage_gte_limit, mintage_lte_limit)

    #Characteristics Search
    if (weight_gte_limit or weight_lte_limit):
        queryset = _get_weight_range_queryset(queryset, weight_gte_limit, weight_lte_limit)
    if (length_gte_limit or length_lte_limit):
        queryset = _get_length_range_queryset(queryset, length_gte_limit, length_lte_limit)
    if (width_gte_limit or width_lte_limit):
        queryset = _get_width_range_queryset(queryset, width_gte_limit, width_lte_limit)
    if (thickness_gte_limit or thickness_lte_limit):
        queryset = _get_thickness_range_queryset(queryset, thickness_gte_limit, thickness_lte_limit)

    return queryset


def get_sub_style_queryset(request):
    queryset  = CoinModel.SubStyle.objects.all()

    parent_style_id = request.query_params.get('parent')

    if parent_style_id:
        return queryset.filter(parent_coin = parent_style_id)

    return queryset


def get_coin_queryset(request):
    queryset = CoinModel.CoinStyle.objects.all()

    #Exact match
    km_number = request.query_params.get('km_number')

    #IF km_number is specified, return an item(usually 1 item)
    if km_number:
        return queryset.filter(km_number = km_number)

    #Ancestors parameters
    region_id             = request.query_params.get('region')
    country_id            = request.query_params.get('country')
    category_id           = request.query_params.get('category')
    collection_id         = request.query_params.get('collection')
    coin_family_id        = request.query_params.get('coin_family')
    minted_by_id          = request.query_params.get('minted_by')

    #Standard Information parameters
    year_gte_limit        = request.query_params.get('year_lte')
    year_lte_limit        = request.query_params.get('year_gte')
    shape_id              = request.query_params.get('shape')
    quality_id            = request.query_params.get('quality')
    edge_id               = request.query_params.get('edge')
    material_id           = request.query_params.get('material')
    standard_gte_limit    = request.query_params.get('standard_lte')
    standard_lte_limit    = request.query_params.get('standard_gte')
    denomination_value    = request.query_params.get('denomination_value')
    denomination_currency = request.query_params.get('denomination_currency')
    mintage_gte_limit     = request.query_params.get('mintage_gte')
    mintage_lte_limit     = request.query_params.get('mintage_lte')

    #Characteristics parameters
    weight_gte_limit      = request.query_params.get('weight_gte')
    weight_lte_limit      = request.query_params.get('weight_lte')
    length_gte_limit      = request.query_params.get('length_gte')
    length_lte_limit      = request.query_params.get('length_lte')
    width_gte_limit       = request.query_params.get('width_gte')
    width_lte_limit       = request.query_params.get('width_lte')
    thickness_gte_limit   = request.query_params.get('thickness_gte')
    thickness_lte_limit   = request.query_params.get('thickness_lte')

    #No KM - process to the filter process
    #Ancestors Search
    if region_id:
        queryset = queryset.filter(coin_family__collection__category__country__region__name__in = _split_string(region_id))
    if country_id:
        queryset = queryset.filter(coin_family__collection__category__country__name__in = _split_string(country_id))
    if category_id:
        queryset = queryset.filter(coin_family__collection__category__name__in = _split_string(category_id))
    if collection_id:
        queryset = queryset.filter(coin_family__collection__name__in = _split_string(collection_id))
    if minted_by_id:
        queryset = queryset.filter(coin_family__minted_by__name__in = _split_string(minted_by_id))

    #Standard Information Search
    if (year_gte_limit or year_lte_limit):
        queryset = _get_year_range_queryset(queryset, year_gte_limit, year_lte_limit)
    if shape_id:
        queryset = queryset.filter(shape__name__in = _split_string(shape_id))
    if quality_id:
        queryset = queryset.filter(quality__name__in = _split_string(quality_id))
    if edge_id:
        queryset = queryset.filter(edge__name__in = _split_string(edge_id))
    if material_id:
        queryset = queryset.filter(material__name__in = _split_string(material_id))
    if (standard_gte_limit or standard_gte_limit):
        queryset = _get_standard_range_queryset(queryset, standard_gte_limit, standard_lte_limit)
    #Filter IF AND ONLY IF there is Denomination Value and Currency
    if (denomination_value and denomination_currency):
        queryset = _get_denomination_queryset(queryset, denomination_value, denomination_currency)
    if (mintage_gte_limit or mintage_lte_limit):
        queryset = _get_mintage_range_queryset(queryset, mintage_gte_limit, mintage_lte_limit)

    #Characteristics Search
    if (weight_gte_limit or weight_lte_limit):
        queryset = _get_weight_range_queryset(queryset, weight_gte_limit, weight_lte_limit)
    if (length_gte_limit or length_lte_limit):
        queryset = _get_length_range_queryset(queryset, length_gte_limit, length_lte_limit)
    if (width_gte_limit or width_lte_limit):
        queryset = _get_width_range_queryset(queryset, width_gte_limit, width_lte_limit)
    if (thickness_gte_limit or thickness_lte_limit):
        queryset = _get_thickness_range_queryset(queryset, thickness_gte_limit, thickness_lte_limit)

    return queryset
