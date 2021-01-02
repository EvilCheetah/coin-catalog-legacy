from rest_framework import status

import coin_catalog.models as CoinModel
import coin_catalog.api.serializers.list_serializers as CoinListSerializer


def _success_create(serializer):
    """
    Returns the serialized 'response_data' and 'status'-code
    When objects is Created
    """
    response_data           = serializer.data
    response_data['status'] = 'Created Successfully'
    return response_data, status.HTTP_201_CREATED


def _success_find(serializer):
    """
    Returns the serialized 'response_data' and 'status'-code
    When objects is Found in DB
    """
    response_data           = serializer.data
    response_data['status'] = 'Already exists in DB'
    return response_data, status.HTTP_302_FOUND


#------------------------POST Functions Themselves------------------------#
"""
    When making a POST request, follows this pattern:
        3) If data is not valid, returns Serializer errors
           (Doesn't check for UniqueTogether)
        1) Checks for existing object in DB
        2) If nothing found, tries to create one
"""
def get_response_for_post_request_for_region_viewset(request):
    """
    This function is designated for
        - Model:   Region
        - Viewset: RegionViewSet
    """
    serializer = CoinListSerializer.RegionSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    region     = CoinModel.Region.objects.filter(
            name__iexact = serializer.validated_data['name']
            )

    if region:
        serializer = CoinListSerializer.RegionSerializer(region.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)


def get_response_for_post_request_for_country_viewset(request):
    """
    This function is designated for
        - Model:   Country
        - Viewset: CountryViewSet
    """
    serializer = CoinListSerializer.CountrySerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    country    = CoinModel.Country.objects.filter(
            region_id    = serializer.validated_data['region'],
            name__iexact = serializer.validated_data['name']
            )

    if country:
        serializer = CoinListSerializer.CountrySerializer(country.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)


def get_response_for_post_request_for_category_viewset(request):
    """
    This function is designated for
        - Model:   Category
        - Viewset: CategoryViewSet
    """
    serializer = CoinListSerializer.CategorySerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    category   = CoinModel.Category.objects.filter(
            country_id   = serializer.validated_data['country'],
            name__iexact = serializer.validated_data['name']
            )

    if category:
        serializer = CoinListSerializer.CategorySerializer(category.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)


def get_response_for_post_request_for_collection_viewset(request):
    """
    This function is designated for
        - Model:   Collection
        - Viewset: CollectionViewSet
    """
    serializer = CoinListSerializer.CollectionSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    collection = CoinModel.Collection.objects.filter(
            category_id  = serializer.validated_data['category'],
            name__iexact = serializer.validated_data['name']
            )

    if collection:
        serializer = CoinListSerializer.CollectionSerializer(collection.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)


def get_response_for_post_request_for_currency_viewset(request):
    """
    This function is designated for
        - Model:   Currency
        - Viewset: CurrencyViewSet
    """
    serializer = CoinListSerializer.CurrencySerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    currency = CoinModel.Currency.objects.filter(
            name__iexact = serializer.validated_data['name']
            )

    if currency:
        serializer = CoinListSerializer.CurrencySerializer(currency.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)


def get_response_for_post_request_for_country_currency_viewset(request):
    """
    This function is designated for
        - Model:   CountryCurrency
        - Viewset: CountryCurrencyViewSet
    """
    serializer = CoinListSerializer.CountryCurrencySerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    country_currency = CoinModel.CountryCurrency.objects.filter(
            country_id  = serializer.validated_data['country'],
            currency_id = serializer.validated_data['currency']
            )

    if country_currency:
        serializer = CoinListSerializer.CountryCurrencySerializer(country_currency.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)


def get_response_for_post_request_for_minted_by_viewset(request):
    """
    This function is designated for
        - Model:   MintedBy
        - Viewset: MintedByViewSet
    """
    serializer = CoinListSerializer.MintedBySerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    minted_by  = CoinModel.MintedBy.objects.filter(
            name__iexact = serializer.validated_data['name']
            )

    if minted_by:
        serializer = CoinListSerializer.MintedBySerializer(minted_by.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)


def get_response_for_post_request_for_designer_name_viewset(request):
    """
    This function is designated for
        - Model:   DesignerName
        - Viewset: DesignerNameViewSet
    """
    serializer    = CoinListSerializer.DesignerNameSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    designer_name = CoinModel.DesignerName.objects.filter(
            name__iexact = serializer.validated_data['name']
            )

    if designer_name:
        serializer = CoinListSerializer.MintedBySerializer(designer_name.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)


def get_response_for_post_request_for_sculptor_name_viewset(request):
    """
    This function is designated for
        - Model:   SculptorName
        - Viewset: SculptorNameViewSet
    """
    serializer    = CoinListSerializer.SculptorNameSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    sculptor_name = CoinModel.SculptorName.objects.filter(
            name__iexact = serializer.validated_data['name']
            )

    if sculptor_name:
        serializer = CoinListSerializer.SculptorNameSerializer(sculptor_name.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)


def get_response_for_post_request_for_material_viewset(request):
    """
    This function is designated for
        - Model:   Material
        - Viewset: MaterialViewSet
    """
    serializer    = CoinListSerializer.MaterialSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    material = CoinModel.Material.objects.filter(
            name__iexact = serializer.validated_data['name']
            )

    if material:
        serializer = CoinListSerializer.MaterialSerializer(material.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)


def get_response_for_post_request_for_quality_viewset(request):
    """
    This function is designated for
        - Model:   Quality
        - Viewset: QualityViewSet
    """
    serializer    = CoinListSerializer.QualitySerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    quality = CoinModel.Quality.objects.filter(
            name__iexact = serializer.validated_data['name']
            )

    if quality:
        serializer = CoinListSerializer.QualitySerializer(quality.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)


def get_response_for_post_request_for_edge_viewset(request):
    """
    This function is designated for
        - Model:   Edge
        - Viewset: EdgeViewSet
    """
    serializer    = CoinListSerializer.EdgeSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    edge = CoinModel.Edge.objects.filter(
            name__iexact = serializer.validated_data['name']
            )

    if edge:
        serializer = CoinListSerializer.EdgeSerializer(edge.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)


def get_response_for_post_request_for_shape_viewset(request):
    """
    This function is designated for
        - Model:   Shape
        - Viewset: ShapeViewSet
    """
    serializer    = CoinListSerializer.ShapeSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    shape = CoinModel.Shape.objects.filter(
            name__iexact = serializer.validated_data['name']
            )

    if shape:
        serializer = CoinListSerializer.ShapeSerializer(shape.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)

def get_response_for_post_request_for_coin_family_viewset(request):
    """
    This function is designated for
        - Model:   CoinFamily
        - Viewset: CoinFamilyViewSet
    """
    serializer    = CoinListSerializer.CoinFamilySerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    coin_family = CoinModel.CoinFamily.objects.filter(
            collection_id = serializer.validated_data['collection'],
            name__iexact  = serializer.validated_data['name']
            )

    if coin_family:
        serializer = CoinListSerializer.CoinFamilySerializer(coin_family.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)


def get_response_for_post_request_for_coin_style_viewset(request):
    """
    This function is designated for
        - Model:   CoinStyle
        - Viewset: CoinStyleViewSet
    """
    serializer    = CoinListSerializer.CoinStyleSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    coin_style = CoinModel.CoinStyle.objects.filter(
            coin_family_id           = serializer.validated_data['coin_family'],
            additional_name__iexact  = serializer.validated_data['additional_name'],
            year                     = serializer.validated_data['year'],
            denomination_value       = serializer.validated_data['denomination_value'],
            denomination_currency_id = serializer.validated_data['denomination_currency'],
            material_id              = serializer.validated_data['material'],
            standard                 = serializer.validated_data['standard'],
            shape_id                 = serializer.validated_data['shape'],
            quality_id               = serializer.validated_data['quality'],
            is_substyle              = serializer.validated_data['is_substyle']
            )

    if coin_style:
        serializer = CoinListSerializer.CoinStyleSerializer(coin_style.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)


def get_response_for_post_request_for_sub_style_viewset(request):
    """
    This function is designated for
        - Model:   SubStyle
        - Viewset: SubStyleViewSet
    """
    print(request.data)

    serializer    = CoinListSerializer.SubStyleSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    sub_style = CoinModel.SubStyle.objects.filter(
            substyle_coin_id = serializer.validated_data['substyle_coin']
            )

    print(sub_style)

    if sub_style:
        serializer = CoinListSerializer.SubStyleSerializer(sub_style.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)


def get_response_for_post_request_for_note_viewset(request):
    """
    This function is designated for
        - Model:   Note
        - Viewset: NoteViewSet
    """
    serializer    = CoinListSerializer.NoteSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    note = CoinModel.Note.objects.filter(
            coin_style_id       = serializer.validated_data['coin_style'],
            description__iexact = serializer.validated_data['description']
            )

    if note:
        serializer = CoinListSerializer.NoteSerializer(note.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)


def get_response_for_post_request_for_side_of_coin_viewset(request):
    """
    This function is designated for
        - Model:   SideOfCoin
        - Viewset: SideOfCoinViewSet
    """
    serializer    = CoinListSerializer.SideOfCoinSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    side_of_coin = CoinModel.SideOfCoin.objects.filter(
            name__iexact = serializer.validated_data['name']
            )

    if side_of_coin:
        serializer = CoinListSerializer.SideOfCoinSerializer(side_of_coin.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)


def get_response_for_post_request_for_coin_designer_viewset(request):
    """
    This function is designated for
        - Model:   CoinDesigner
        - Viewset: CoinDesignerViewSet
    """
    serializer    = CoinListSerializer.CoinAllDesignersSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    coin_designer = CoinModel.CoinDesigner.objects.filter(
            coin_style_id = serializer.validated_data['coin_style'],
            side_id       = serializer.validated_data['side'],
            designer_id   = serializer.validated_data['designer']
            )

    if coin_designer:
        serializer = CoinListSerializer.CoinAllDesignersSerializer(coin_designer.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)


def get_response_for_post_request_for_coin_sculptor_viewset(request):
    """
    This function is designated for
        - Model:   CoinSculptor
        - Viewset: CoinSculptorViewSet
    """
    serializer    = CoinListSerializer.CoinAllSculptorsSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    coin_sculptor = CoinModel.CoinSculptor.objects.filter(
            coin_style_id = serializer.validated_data['coin_style'],
            side_id       = serializer.validated_data['side'],
            sculptor_id   = serializer.validated_data['sculptor']
            )

    if coin_sculptor:
        serializer = CoinListSerializer.CoinAllSculptorsSerializer(coin_sculptor.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)


def get_response_for_post_request_for_image_viewset(request):
    """
    This function is designated for
        - Model:   Image
        - Viewset: ImageViewSet
    """
    serializer    = CoinListSerializer.ImageSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)

    image = CoinModel.Image.objects.filter(
            coin_style_id = serializer.validated_data['coin_style'],
            side_id       = serializer.validated_data['side']
            )

    if image:
        serializer = CoinListSerializer.ImageSerializer(image.first())
        return _success_find(serializer)

    serializer.save()
    return _success_create(serializer)
