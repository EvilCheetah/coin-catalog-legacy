from rest_framework.response import Response

import coin_catalog.models as CoinModel
import coin_catalog.services.exceptions as Exception
import coin_catalog.api.serializers.list_serializers as CoinListSerializer

SPLIT_CHAR = ','


##----------------------Private Functions----------------------##
def _split_string(item: str) -> list:
    return item.split(SPLIT_CHAR)


##-----------------------Range Functions-----------------------##
def _get_year_range_queryset(queryset, year_gte_limit, year_lte_limit):
    try:
        if ( year_gte_limit ):
            queryset = queryset.filter(year__gte = int(year_gte_limit))
        if ( year_lte_limit ):
            queryset = queryset.filter(year__lte = int(year_lte_limit))

        return queryset

    except ValueError:
        Exception.type_error_for_integer_range_parameter('year')


def _get_standard_range_queryset(queryset, standard_gte_limit, standard_lte_limit):
    try:
        if ( standard_gte_limit ):
            queryset = queryset.filter(standard__gte = float(standard_gte_limit))
        if ( standard_lte_limit ):
            queryset = queryset.filter(standard__lte = float(standard_lte_limit))

        return queryset

    except ValueError:
        Exception.type_error_for_float_range_parameter('standard')


def _get_denomination_queryset(queryset, denomination_value, denomination_currency):
    try:
        queryset = queryset.filter(denomination_value = denomination_value)
    except ValueError:
        Exception.type_error_for_integer_parameter('denomination_value')

    try:
        queryset = queryset.filter(denomination_currency__currency__id = denomination_currency)
    except ValueError:
        Exception.type_error_for_integer_parameter('denomination_currency')

    return queryset


def _get_mintage_range_queryset(queryset, mintage_gte_limit, mintage_lte_limit):
    try:
        if ( mintage_gte_limit ):
            queryset = queryset.filter(mintage__gte = int(mintage_gte_limit))
        if ( mintage_lte_limit ):
            queryset = queryset.filter(mintage__lte = int(mintage_lte_limit))

        return queryset

    except ValueError:
        Exception.type_error_for_integer_range_parameter('mintage')


def _get_weight_range_queryset(queryset, weight_gte_limit, weight_lte_limit):
    try:
        if ( weight_gte_limit ):
                queryset = queryset.filter(weight__gte = float(weight_gte_limit))
        if ( weight_lte_limit ):
            queryset = queryset.filter(weight__lte = float(weight_lte_limit))

        return queryset

    except ValueError:
        Exception.type_error_for_float_range_parameter('weight')


def _get_length_range_queryset(queryset, length_gte_limit, length_lte_limit):
    if ( length_gte_limit ):
        try:
            queryset = queryset.filter(length__gte = float(length_gte_limit))
        except ValueError:
            Exception.type_error_for_float_range_parameter('length_gte')

    if ( length_lte_limit ):
        try:
            queryset = queryset.filter(length__lte = float(length_lte_limit))
        except ValueError:
            Exception.type_error_for_float_range_parameter('length__lte')

    return queryset


def _get_width_range_queryset(queryset, width_gte_limit, width_lte_limit):
    try:
        if ( width_gte_limit ):
            queryset = queryset.filter(width__gte = float(width_gte_limit))
        if ( width_lte_limit ):
            queryset = queryset.filter(width__lte = float(width_lte_limit))

        return queryset

    except ValueError:
        Exception.type_error_for_float_range_parameter('width')


def _get_thickness_range_queryset(queryset, thickness_gte_limit, thickness_lte_limit):
    try:
        if ( thickness_gte_limit ):
            queryset = queryset.filter(thickness__gte = float(thickness_gte_limit))
        if ( thickness_lte_limit ):
            queryset = queryset.filter(thickness__lte = float(thickness_lte_limit))

        return queryset

    except ValueError:
        Exception.type_error_for_float_range_parameter('thickness')


##--------------------Descendants-Dedicated Functions--------------------##
def _get_queryset_based_on_coin_style(request, queryset):
    coin_style = request.query_params.get('coin_style')

    if ( coin_style ):
        queryset = queryset.filter(coin_style_id = coin_style)

    return queryset

############################################################################
##########################END OF PRIVATE FUNCTIONS##########################
############################################################################


##----------------------Queryset Functions----------------------##
def get_region_queryset(request):
    queryset    = CoinModel.Region.objects.all()

    region_name = request.query_params.get('region')

    if region_name:
        queryset = queryset.filter(name__in = _split_string(region_name))

    return queryset


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

    if region_id:
        queryset = queryset.filter(collection__category__country__region__id__in = _split_string(region_id))

    if country_id:
        queryset = queryset.filter(collection__category__country__id__in = _split_string(country_id))

    if category_id:
        queryset = queryset.filter(collection__category__id__in = _split_string(category_id))

    if collection_id:
        queryset = queryset.filter(collection__id__in = _split_string(collection_id))

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
    year_gte_limit        = request.query_params.get('year_gte')
    year_lte_limit        = request.query_params.get('year_lte')
    shape_id              = request.query_params.get('shape')
    quality_id            = request.query_params.get('quality')
    edge_id               = request.query_params.get('edge')
    material_id           = request.query_params.get('material')
    standard_gte_limit    = request.query_params.get('standard_gte')
    standard_lte_limit    = request.query_params.get('standard_lte')
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
        try:
            queryset = queryset.filter(coin_family__collection__category__country__region__id__in = _split_string(region_id))
        except ValueError:
            Exception.type_error_for_list_parameter('region')

    if country_id:
        try:
            queryset = queryset.filter(coin_family__collection__category__country__id__in = _split_string(country_id))
        except ValueError:
            Exception.type_error_for_list_parameter('country')

    if category_id:
        try:
            queryset = queryset.filter(coin_family__collection__category__id__in = _split_string(category_id))
        except ValueError:
            Exception.type_error_for_list_parameter('category')

    if collection_id:
        try:
            queryset = queryset.filter(coin_family__collection__id__in = _split_string(collection_id))
        except ValueError:
            Exception.type_error_for_list_parameter('collection')

    if coin_family_id:
        try:
            queryset = queryset.filter(coin_family__id__in = _split_string(coin_family_id))
        except ValueError:
            Exception.type_error_for_list_parameter('coin_family')

    if minted_by_id:
        try:
            queryset = queryset.filter(minted_by__id__in = _split_string(minted_by_id))
        except ValueError:
            Exception.type_error_for_list_parameter('minted_by')

    #Standard Information Search
    if (year_gte_limit or year_lte_limit):
        #checks error in _get_year_range_queryset
        queryset = _get_year_range_queryset(queryset, year_gte_limit, year_lte_limit)

    if shape_id:
        try:
            queryset = queryset.filter(shape__id__in = _split_string(shape_id))
        except ValueError:
            Exception.type_error_for_list_parameter('shape')

    if quality_id:
        try:
            queryset = queryset.filter(quality__id__in = _split_string(quality_id))
        except ValueError:
            Exception.type_error_for_list_parameter('quality')

    if edge_id:
        try:
            queryset = queryset.filter(edge__id__in = _split_string(edge_id))
        except ValueError:
            Exception.type_error_for_list_parameter('edge')

    if material_id:
        try:
            queryset = queryset.filter(material__id__in = _split_string(material_id))
        except ValueError:
            Exception.type_error_for_list_parameter('material')

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


def get_note_queryset(request):
    queryset = CoinModel.Note.objects.all()

    return _get_queryset_based_on_coin_style(request, queryset)


def get_coin_designer_queryset(request):
    queryset = CoinModel.CoinDesigner.objects.all()

    return _get_queryset_based_on_coin_style(request, queryset)


def get_coin_sculptor_queryset(request):
    queryset = CoinModel.CoinSculptor.objects.all()

    return _get_queryset_based_on_coin_style(request, queryset)


def get_image_queryset(request):
    queryset = CoinModel.Image.objects.all()

    return _get_queryset_based_on_coin_style(request, queryset)


def get_full_info_coin_queryset(request):
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
        queryset = queryset.filter(minted_by__name__in = _split_string(minted_by_id))

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
