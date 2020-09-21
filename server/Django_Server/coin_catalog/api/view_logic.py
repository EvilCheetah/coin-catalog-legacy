from django.db.models import Q

import coin_catalog.models as CoinModel
import coin_catalog.api.serializers.list_serializers as CoinListSerializer

CHAR_SPLIT_CHAR = ','
NUM_SPLIT_CHAR  = '-'

##----------------------Private Functions----------------------##
def _split_string(item: str) -> list:
    return item.split(CHAR_SPLIT_CHAR)


def _split_numbers(items: str) -> list:
    return items.split(NUM_SPLIT_CHAR)


def _get_year_range_queryset(queryset, year_range):
    year_range = _split_numbers(year_range)

    if ( len(year_range) == 1 ):
        return queryset

    if ( year_range[0] != ''):
        queryset = queryset.filter(year__gte = int(year_range[0]))

    if ( year_range[1] != ''):
        queryset = queryset.filter(year__lte = int(year_range[1]))

    return queryset


def _get_standard_range_queryset(queryset, standard_range):
    standard_range = _split_numbers(standard_range)

    if ( len(standard_range) == 1):
        return queryset

    if ( standard_range[0] != ''):
        queryset = queryset.filter(standard__gte = float(standard_range[0]))

    if ( standard_range[1] != ''):
        queryset = queryset.filter(standard__lte = float(standard_range[1]))

    return queryset


def _get_mintage_range_queryset(queryset, mintage_range):
    mintage_range = _split_numbers(mintage_range)

    if ( len(mintage_range) == 1):
        return queryset

    if ( mintage_range[0] != ''):
        queryset = queryset.filter(mintage__gte = int(mintage_range[0]))

    if ( mintage_range[1] != ''):
        queryset = queryset.filter(mintage__lte = int(mintage_range[1]))

    return queryset


def _get_weight_range_queryset(queryset, weight_range):
    weight_range = _split_numbers(weight_range)

    if ( len(weight_range) == 1):
        return queryset

    if ( weight_range[0] != ''):
        queryset = queryset.filter(weight__gte = float(weight_range[0]))

    if ( weight_range[1] != ''):
        queryset = queryset.filter(weight__lte = float(weight_range[1]))

    return queryset


def _get_length_range_queryset(queryset, length_range):
    length_range = _split_numbers(length_range)

    if ( len(length_range) == 1):
        return queryset

    if ( length_range[0] != ''):
        queryset = queryset.filter(length__gte = float(length_range[0]))

    if ( length_range[1] != ''):
        queryset = queryset.filter(length__lte = float(length_range[1]))

    return queryset


def _get_width_range_queryset(queryset, width_range):
    width_range = _split_numbers(width_range)

    if ( len(width_range) == 1):
        return queryset

    if ( width_range[0] != ''):
        queryset = queryset.filter(width__gte = float(width_range[0]))

    if ( width_range[1] != ''):
        queryset = queryset.filter(width__lte = float(width_range[1]))

    return queryset


def _get_thickness_range_queryset(queryset, thickness_range):
    thickness_range = _split_numbers(thickness_range)

    if ( len(thickness_range) == 1):
        return queryset

    if ( thickness_range[0] != ''):
        queryset = queryset.filter(thickness__gte = float(thickness_range[0]))

    if ( thickness_range[1] != ''):
        queryset = queryset.filter(thickness__lte = float(thickness_range[1]))

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
    """
    CoinStyle Queryset Filtering.

    Accepts these parameters:
        Priotiry Items:
         - km_number:
                $ Accepts: STR parameter
                $ Returns: A CoinStyle object that has given KM Number or NONE
                $ ignores any other parameter

        Second Priotiry Parameters
         - region:
                $ Accepts: Region ID, or a
                           List of Region IDs, separated with ','
                           e.g. "region=1,2"

         - country:
                $ Accepts: Country ID, or a
                           List of Country IDs, separated with ','
                           e.g. "country=1,2"

         - category:
                $ Accepts: Category ID, or a
                           List of Category IDs, separated with ','
                           e.g. "category=1,2"

         - collection
                $ Accepts: Collection ID, or a
                           List of Collection IDs, separated with ','
                           e.g. "collection=1,2"

         - coin_family
                $ Accepts: CoinFamily ID, or a
                           List of CoinFamily IDs, separated with ','
                           e.g. "coin_family=1,2"

         - minted_by
                $ Accepts: MintedBy ID, or a
                           List of MintedBy IDs, separated with ','
                           e.g. "minted_by=1,2"

         - year
                $ Accepts: An INTEGER Year range, separated with '-'
                           e.g. "year=1999-2000",   Math notation - year ∈ [1999, 2000]
                                "year=-1999",       Math notation - year <= 1999
                                "year=1891-"        Math notation - year >= 1999

         - shape
                $ Accepts: Shape ID, or a
                           List of Shape IDs, separated with ','
                           e.g. "shape=1,2"

         - quality
                $ Accepts: Quality ID, or a
                           List of Quality IDs, separated with ','
                           e.g. "quality=1,2"

         - edge
                $ Accepts: Edge ID, or a
                           List of Edge IDs, separated with ','
                           e.g. "edge=1,2"

         - material
                $ Accepts: Material ID, or a
                           List of Material IDs, separated with ','
                           e.g. "material=1,2"

         - standard
                $ Accepts: A FLOAT Standard range, separated with '-'
                           e.g. "standard=0-999.9",   Math notation - standard ∈ [0, 999.9]
                                "standard=-825",      Math notation - standard <= 825
                                "standard=965-"       Math notation - standard >= 965

         - denomination
                $ Accepts: STR Denomination Parameter, or a
                           List of STR Denomination Parameters, separated with ','
                           e.g. "denomination=20 BYN",
                                "denomination=20 USD,30 AUD"

         - mintage
                $ Accepts: An INTEGER Mintage range, separated with '-'
                           e.g. "mintage=10-20000",   Math notation - mintage ∈ [10, 20000]
                                "mintage=-3000",      Math notation - mintage <= 3000
                                "mintage=500-"        Math notation - mintage >= 500


         - weight
                $ Accepts: A FLOAT Weight range, separated with '-'
                           e.g. "weight=0-150",   Math notation - weight ∈ [0, 150]
                                "weight=80.0-"    Math notation - weight >= 80.0
                                "weight=-33.3",   Math notation - weight <= 33.3


         - length
                $ Accepts: A FLOAT Length range, separated with '-'
                           e.g. "length=0-150",   Math notation - length ∈ [0, 150]
                                "length=80.0-"    Math notation - length >= 80.0
                                "length=-33.3",   Math notation - length <= 33.3

         - width
                $ Accepts: A FLOAT Width range, separated with '-'
                           e.g. "width=0-150",   Math notation - width ∈ [0, 150]
                                "width=80.0-"    Math notation - width >= 80.0
                                "width=-33.3",   Math notation - width <= 33.3

         - thickness
                $ Accepts: A FLOAT Thickness range, separated with '-'
                           e.g. "thickness=0-150",   Math notation - thickness ∈ [0, 150]
                                "thickness=80.0-"    Math notation - thickness >= 80.0
                                "thickness=-33.3",   Math notation - thickness <= 33.3

        SECOND PRIORITY ITEMS CAN BE COMBINED TOGETHER
    """
    queryset = CoinModel.CoinStyle.objects.all()

    #Exact match
    km_number        = request.query_params.get('km_number')

    #IF km_number is specified, return an item(usually 1 item)
    if km_number:
        return queryset.filter(km_number = km_number)

    #Ancestors parameters
    region_id        = request.query_params.get('region')
    country_id       = request.query_params.get('country')
    category_id      = request.query_params.get('category')
    collection_id    = request.query_params.get('collection')
    coin_family_id   = request.query_params.get('coin_family')
    minted_by_id     = request.query_params.get('minted_by')

    #Standard Information parameters
    year_range       = request.query_params.get('year')
    shape_id         = request.query_params.get('shape')
    quality_id       = request.query_params.get('quality')
    edge_id          = request.query_params.get('edge')
    material_id      = request.query_params.get('material')
    standard_range   = request.query_params.get('standard')
    denomination     = request.query_params.get('denomination')
    mintage_range    = request.query_params.get('mintage')

    #Characteristics parameters
    weight_range     = request.query_params.get('weight')
    length_range     = request.query_params.get('length')
    width_range      = request.query_params.get('width')
    thickness_range  = request.query_params.get('thickness')

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
    if year_range:
        queryset = _get_year_range_queryset(queryset, year_range)
    if shape_id:
        queryset = queryset.filter(shape__id__in = _split_string(shape_id))
    if quality_id:
        queryset = queryset.filter(quality__id__in = _split_string(quality_id))
    if edge_id:
        queryset = queryset.filter(edge__id__in = _split_string(edge_id))
    if material_id:
        queryset = queryset.filter(material__id__in = _split_string(material_id))
    if standard_range:
        queryset = _get_standard_range_queryset(queryset, standard_range)
    if denomination:
        queryset = queryset.filter(denomination__in = _split_string(denomintation))
    if mintage_range:
        queryset = _get_mintage_range_queryset(queryset, mintage_range)

    #Characteristics Search
    if weight_range:
        queryset = _get_weight_range_queryset(queryset, weight_range)
    if length_range:
        queryset = _get_length_range_queryset(queryset, length_range)
    if width_range:
        queryset = _get_width_range_queryset(queryset, width_range)
    if thickness_range:
        queryset = _get_thickness_range_queryset(queryset, thickness_range)

    return queryset
