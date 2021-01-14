# Django Imports
from django.shortcuts import get_object_or_404

# REST Imports
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from accounts.permissions import (
    IsAuthenticated,
    IsStaffUser,
    IsAdminUser
)

# Model Imports
import coin_catalog.models as CoinModel

# Serializer Imports
import coin_catalog.api.serializers.list_serializers as CoinListSerializer
import coin_catalog.api.serializers.instance_serializers as CoinInstanceSerializer

# Services Imports
import coin_catalog.services.view_logic.list_logic as List
import coin_catalog.services.view_logic.instance_logic as Instance
import coin_catalog.services.view_logic.post_logic as Create
import coin_catalog.services.view_logic.delete_logic as Delete
import coin_catalog.services.view_logic.update_logic as Update

# Pagination Imports
from coin_catalog.api.pagination import (
    StandardResultsSetPagination,
    InformationResultsSetPagination,
    FullInformationResultsSetPagination
)


class BaseModelViewSet(viewsets.ModelViewSet):
    """
        BaseModelViewSet is created for the permission purposes,
        in order to clutter up the ViewSets with 'get_permissions'
        method and set general permission for each method in ViewSet

        Methods:
            - 'create'          - Staff Users only
            - 'destroy'         - Admin Users only
            - 'list'            - Authenticated Users only
            - 'partial_update'  - Staff Users only
            - 'retrieve'        - Authenticated Users only
            - 'update'          - Staff Users only
    """
    create_method         = None
    destroy_method        = None
    update_method         = None
    partial_update_method = update_method

    def create(self, request):
        assert self.create_method is not None, (
            f"{self.__class__.__name__} should include `create_method` attribute, "
            "or override `create()` function"
        )
        response_data, status = self.create_method.get_response(request)
        return Response(response_data, status)

    def destroy(self, request, pk):
        assert self.destroy_method is not None, (
            f"{self.__class__.__name__} should include `destroy_method` attribute, "
            "or override `destroy()` function"
        )
        response_data, status = self.destroy_method.get_response(pk, request)
        return Response(response_data, status = status)

    def update(self, request, pk):
        assert self.update_method is not None, (
            f"{self.__class__.__name__} should include `update_method` attribute, "
            "or override `update()` function"
        )
        response_data, status = self.update_method.get_response(pk, request)
        return Response(response_data, status)

    def partial_update(self, request, pk):
        assert self.partial_update_method is not None, (
            f"{self.__class__.__name__} should include `partial_update_method` attribute, "
            "or override `partial_update()` function"
        )
        response_data, status = self.partial_update_method.get_response(pk, request, partial = True)
        return Response(response_data, status)

    permission_classes_by_action = {
        'create':           [IsStaffUser],
        'destroy':          [IsAdminUser],
        'list':             [IsAuthenticated],
        'partial_update':   [IsStaffUser],
        'retrieve':         [IsAuthenticated],
        'update':           [IsStaffUser],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


##-------------------Model Based View Sets-------------------##
"""
These ViewSets are designated for pure model output
"""
class RegionViewSet(BaseModelViewSet):
    """
        This ViewSet is used to handle the actions for 'Region' Model
    """
    queryset         = CoinModel.Region.objects.all()
    serializer_class = CoinListSerializer.RegionSerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.RegionPostRequest
    destroy_method        = Delete.RegionDeleteRequest
    update_method         = Update.RegionUpdateRequest
    partial_update_method = Update.RegionUpdateRequest

    def list(self, request):
        queryset   = List.get_region_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.RegionSerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.Region.objects.all()
        region     = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.RegionSerializer(region)
        return Response(serializer.data)


class CountryViewSet(BaseModelViewSet):
    queryset         = CoinModel.Country.objects.all()
    serializer_class = CoinListSerializer.CountrySerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.CountryPostRequest
    destroy_method        = Delete.CountryDeleteRequest
    update_method         = Update.CountryUpdateRequest
    partial_update_method = Update.CountryUpdateRequest

    def list(self, request):
        queryset   = List.get_country_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.CountrySerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.Country.objects.all()
        country    = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.CountrySerializer(country)
        return Response(serializer.data)


class CategoryViewSet(BaseModelViewSet):
    queryset         = CoinModel.Category.objects.all()
    serializer_class = CoinListSerializer.CategorySerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.CategoryPostRequest
    destroy_method        = Delete.CategoryDeleteRequest
    update_method         = Update.CategoryUpdateRequest
    partial_update_method = Update.CategoryUpdateRequest

    def list(self, request):
        queryset   = List.get_category_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.CategorySerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.Category.objects.all()
        category   = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.CategorySerializer(category)
        return Response(serializer.data)


class CollectionViewSet(BaseModelViewSet):
    queryset         = CoinModel.Collection.objects.all()
    serializer_class = CoinListSerializer.CollectionSerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.CollectionPostRequest
    destroy_method        = Delete.CollectionDeleteRequest
    update_method         = Update.CollectionUpdateRequest
    partial_update_method = Update.CollectionUpdateRequest

    def list(self, request):
        queryset   = List.get_collection_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.CollectionSerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.Collection.objects.all()
        collection = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.CollectionSerializer(collection)
        return Response(serializer.data)


class CurrencyViewSet(BaseModelViewSet):
    queryset         = CoinModel.Currency.objects.all()
    serializer_class = CoinListSerializer.CurrencySerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.CurrencyPostRequest
    destroy_method        = Delete.CurrencyDeleteRequest
    update_method         = Update.CurrencyUpdateRequest
    partial_update_method = Update.CurrencyUpdateRequest

    def list(self, request):
        queryset   = List.get_currency_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.CurrencySerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset = CoinModel.Currency.objects.all()
        currency = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.CurrencySerializer(currency)
        return Response(serializer.data)


class CountryCurrencyViewSet(BaseModelViewSet):
    queryset         = CoinModel.CountryCurrency.objects.all()
    serializer_class = CoinListSerializer.CountryCurrencySerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.CountryCurrencyPostRequest
    destroy_method        = Delete.CountryCurrencyDeleteRequest
    update_method         = Update.CountryCurrencyUpdateRequest
    partial_update_method = Update.CountryCurrencyUpdateRequest

    def list(self, request):
        queryset   = List.get_country_currency_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.CountryCurrencySerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset         = CoinModel.CountryCurrency.objects.all()
        country_currency = get_object_or_404(queryset, pk = pk)
        serializer       = CoinInstanceSerializer.CountryCurrencySerializer(country_currency)
        return Response(serializer.data)


class MintedByViewSet(BaseModelViewSet):
    queryset         = CoinModel.MintedBy.objects.all()
    serializer_class = CoinListSerializer.MintedBySerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.MintedByPostRequest
    destroy_method        = Delete.MintedByDeleteRequest
    update_method         = Update.MintedByUpdateRequest
    partial_update_method = Update.MintedByUpdateRequest

    def list(self, request):
        queryset   = List.get_minted_by_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.MintedBySerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.MintedBy.objects.all()
        minted_by  = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.MintedBySerializer(minted_by)
        return Response(serializer.data)


class DesignerNameViewSet(BaseModelViewSet):
    queryset         = CoinModel.DesignerName.objects.all()
    serializer_class = CoinListSerializer.DesignerNameSerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.DesingerNamePostRequest
    destroy_method        = Delete.DesignerNameDeleteRequest
    update_method         = Update.DesignerNameUpdateRequest
    partial_update_method = Update.DesignerNameUpdateRequest

    def list(self, request):
        queryset   = List.get_designer_name_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.DesignerNameSerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset      = CoinModel.DesignerName.objects.all()
        designer_name = get_object_or_404(queryset, pk = pk)
        serializer    = CoinInstanceSerializer.DesignerNameSerializer(designer_name)
        return Response(serializer.data)


class SculptorNameViewSet(BaseModelViewSet):
    queryset         = CoinModel.SculptorName.objects.all()
    serializer_class = CoinListSerializer.SculptorNameSerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.SculptorNamePostRequest
    destroy_method        = Delete.SculptorNameDeleteRequest
    update_method         = Update.SculptorNameUpdateRequest
    partial_update_method = Update.SculptorNameUpdateRequest

    def list(self, request):
        queryset   = List.get_sculptor_name_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.SculptorNameSerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset      = CoinModel.SculptorName.objects.all()
        sculptor_name = get_object_or_404(queryset, pk = pk)
        serializer    = CoinInstanceSerializer.SculptorNameSerializer(sculptor_name)
        return Response(serializer.data)


class MaterialViewSet(BaseModelViewSet):
    queryset         = CoinModel.Material.objects.all()
    serializer_class = CoinListSerializer.MaterialSerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.MaterialPostRequest
    destroy_method        = Delete.MaterialDeleteRequest
    update_method         = Update.MaterialUpdateRequest
    partial_update_method = Update.MaterialUpdateRequest

    def list(self, request):
        queryset   = List.get_material_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.MaterialSerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.Material.objects.all()
        material   = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.MaterialSerializer(material)
        return Response(serializer.data)


class QualityViewSet(BaseModelViewSet):
    queryset         = CoinModel.Quality.objects.all()
    serializer_class = CoinListSerializer.QualitySerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.QualityPostRequest
    destroy_method        = Delete.QualityDeleteRequest
    update_method         = Update.QualityUpdateRequest
    partial_update_method = Update.QualityUpdateRequest

    def list(self, request):
        queryset   = List.get_quality_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.QualitySerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.Quality.objects.all()
        qualtity   = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.QualitySerializer(qualtity)
        return Response(serializer.data)


class EdgeViewSet(BaseModelViewSet):
    queryset         = CoinModel.Edge.objects.all()
    serializer_class = CoinListSerializer.EdgeSerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.EdgePostRequest
    destroy_method        = Delete.EdgeDeleteRequest
    update_method         = Update.EdgeUpdateRequest
    partial_update_method = Update.EdgeUpdateRequest

    def list(self, request):
        queryset   = List.get_edge_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.EdgeSerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.Edge.objects.all()
        edge       = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.EdgeSerializer(edge)
        return Response(serializer.data)


class ShapeViewSet(BaseModelViewSet):
    queryset         = CoinModel.Shape.objects.all()
    serializer_class = CoinListSerializer.ShapeSerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.ShapePostRequest
    destroy_method        = Delete.ShapeDeleteRequest
    update_method         = Update.ShapeUpdateRequest
    partial_update_method = Update.ShapeUpdateRequest

    def list(self, request):
        queryset   = List.get_shape_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.ShapeSerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.Shape.objects.all()
        shape      = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.ShapeSerializer(edge)
        return Response(serializer.data)


class CoinFamilyViewSet(BaseModelViewSet):
    queryset         = CoinModel.CoinFamily.objects.all()
    serializer_class = CoinListSerializer.CoinFamilySerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.CoinFamilyPostRequest
    destroy_method        = Delete.CoinFamilyDeleteRequest
    update_method         = Update.CoinFamilyUpdateRequest
    partial_update_method = Update.CoinFamilyUpdateRequest

    def list(self, request):
        queryset   = List.get_coin_family_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.CoinFamilySerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset    = CoinModel.CoinFamily.objects.all()
        coin_family = get_object_or_404(queryset, pk = pk)
        serializer  = CoinInstanceSerializer.CountrySerializer(coin_family)
        return Response(serializer.data)


class CoinStyleViewSet(BaseModelViewSet):
    queryset         = CoinModel.CoinStyle.objects.all()
    serializer_class = CoinListSerializer.CoinStyleSerializer

    create_method         = Create.CoinStylePostRequest
    destroy_method        = Delete.CoinStyleDeleteRequest
    update_method         = Update.CoinStyleUpdateRequest
    partial_update_method = Update.CoinStyleUpdateRequest

    def list(self, request):
        queryset   = List.get_coin_style_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.CoinStyleSerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.CoinStyle.objects.all()
        coin_style = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.CoinStyleSerializer(coin_style)
        return Response(serializer.data)


class SubStyleViewSet(BaseModelViewSet):
    queryset         = CoinModel.SubStyle.objects.all()
    serializer_class = CoinListSerializer.SubStyleSerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.SubStylePostRequest
    destroy_method        = Delete.SubStyleDeleteRequest
    update_method         = Update.SubStyleUpdateRequest
    partial_update_method = Update.SubStyleUpdateRequest

    def list(self, request):
        queryset   = List.get_sub_style_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.SubStyleSerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.SubStyle.objects.all()
        sub_style  = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.SubStyleSerializer(sub_style)
        return Response(serializer.data)


class NoteViewSet(BaseModelViewSet):
    queryset         = CoinModel.Note.objects.all()
    serializer_class = CoinListSerializer.NoteSerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.NotePostRequest
    destroy_method        = Delete.NoteDeleteRequest
    update_method         = Update.NoteUpdateRequest
    partial_update_method = Update.NoteUpdateRequest

    def list(self, request):
        queryset   = List.get_note_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.NoteSerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.Note.objects.all()
        note       = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.NoteSerializer(note)
        return Response(serializer.data)


class SideOfCoinViewSet(BaseModelViewSet):
    queryset         = CoinModel.SideOfCoin.objects.all()
    serializer_class = CoinListSerializer.SideOfCoinSerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.SideOfCoinPostRequest
    destroy_method        = Delete.SideOfCoinDeleteRequest
    update_method         = Update.SideOfCoinUpdateRequest
    partial_update_method = Update.SideOfCoinUpdateRequest

    def list(self, request):
        queryset   = List.get_side_of_coin_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.SideOfCoinSerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset     = CoinModel.SideOfCoin.objects.all()
        side_of_coin = get_object_or_404(queryset, pk = pk)
        serializer   = CoinInstanceSerializer.SideOfCoinSerializer(side_of_coin)
        return Response(serializer.data)


class CoinDesignerViewSet(BaseModelViewSet):
    queryset         = CoinModel.CoinDesigner.objects.all()
    serializer_class = CoinListSerializer.CoinAllDesignersSerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.CoinDesignerPostRequest
    destroy_method        = Delete.CoinDesignerDeleteRequest
    update_method         = Update.CoinDesignerUpdateRequest
    partial_update_method = Update.CoinDesignerUpdateRequest

    def list(self, request):
        queryset   = List.get_coin_designer_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.CoinAllDesignersSerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.CoinDesigner.objects.all()
        designer   = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.CoinAllDesignersSerializer(designer)
        return Response(serializer.data)


class CoinSculptorViewSet(BaseModelViewSet):
    queryset         = CoinModel.CoinSculptor.objects.all()
    serializer_class = CoinListSerializer.CoinAllSculptorsSerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.CoinSculptorPostRequest
    destroy_method        = Delete.CoinSculptorDeleteRequest
    update_method         = Update.CoinSculptorUpdateRequest
    partial_update_method = Update.CoinSculptorUpdateRequest

    def list(self, request):
        queryset   = List.get_coin_sculptor_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.CoinAllSculptorsSerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.CoinSculptor.objects.all()
        sculptor   = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.CoinAllSculptorsSerializer(sculptor)
        return Response(serializer.data)


class ImageViewSet(BaseModelViewSet):
    queryset         = CoinModel.Image.objects.all()
    serializer_class = CoinListSerializer.ImageSerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.ImagePostRequest
    destroy_method        = Delete.ImageDeleteRequest
    update_method         = Update.ImageUpdateRequest
    partial_update_method = Update.ImageUpdateRequest

    def list(self, request):
        queryset   = List.get_image_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinListSerializer.ImageSerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.Image.objects.all()
        image      = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.ImageSerializer(image)
        return Response(serializer.data)


##--------------------PreLoaded View Sets--------------------##
"""
These ViewSets are designated to avoid async errors with
requests
"""
class PreLoadedCoinFamilyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CoinInstanceSerializer.PreLoadedCoinFamilySerializer

    def get_queryset(self):
        return None

    def retrieve(self, request, pk = None):
        queryset    = CoinModel.CoinFamily.objects.all()
        coin_family = get_object_or_404(queryset, pk = pk)
        serializer  = CoinInstanceSerializer.PreLoadedCoinFamilySerializer(coin_family)
        return Response(serializer.data)


class PreLoadedCoinStyleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CoinInstanceSerializer.PreLoadedCoinStyleSerializer

    def get_queryset(self):
        return None

    def retrieve(self, request, pk = None):
        queryset    = CoinModel.CoinStyle.objects.all()
        coin_style  = get_object_or_404(queryset, pk = pk)
        serializer  = CoinInstanceSerializer.PreLoadedCoinStyleSerializer(coin_style)
        return Response(serializer.data)


class FullInfoCoinViewSet(viewsets.ReadOnlyModelViewSet):
    """
        This ViewSet is designated to output fully rendered CoinStyle Model

        List:
            = Pagination:
                - Minimum Items per page: 10
                - Maximum Items per page: 100

            = Accepts following queries for Filtering:
                - page_size     - an 'int' in range [10, 100]
                - region        - a 'list' of 'str' of names of regions
                - country       - a 'list' of 'str' of names of countries
                - category      - a 'list' of 'str' of names of categories
                - collections   - a 'list' of 'str' of names of collections
                - coin_family   - a 'list' of 'str' of names of coin families
                - minted_by     - a 'list' of 'str' of names of mints
                - shape         - a 'list' of 'str' of names of shapes
                - quality       - a 'list' of 'str' of names of mint qualities
                - material      - a 'list' of 'str' of names of materials
                - standard_min  - a 'float' of standard minimum value
                - standard_max  - a 'float' of standard maximum value
                - year_min      - an 'int' of year minimum value
                - year_max      - an 'int' of year maximum value
                - denomination  - is either:
                    # SINGLE denomination_value AND SINGLE denomination_currency
                    OR
                    # a 'list' of denomination_currencies
                - mintage_min   - an 'int' of mintage minimum value
                - mintage_max   - an 'int' of mintage maximum  value
                - weight_min    - an 'int' of weight minimum value
                - weight_max    - an 'int' of weight maximum  value
                - length_min    - an 'int' of length minimum value
                - length_max    - an 'int' of length maximum  value
                - width_min     - an 'int' of width minimum value
                - width_max     - an 'int' of width maximum  value
                - thickness_min - an 'int' of thickness minimum value
                - thickness_max - an 'int' of thickness maximum  value
    """
    queryset         = CoinModel.CoinStyle.objects.all()
    serializer_class = CoinInstanceSerializer.FullInfoCoinSerializer
    pagination_class = FullInformationResultsSetPagination

    def list(self, request):
        queryset   = List.get_full_info_coin_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = CoinInstanceSerializer.FullInfoCoinSerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset    = CoinModel.CoinStyle.objects.all()
        coin_style  = get_object_or_404(queryset, pk = pk)
        serializer  = CoinInstanceSerializer.FullInfoCoinSerializer(coin_style)
        return Response(serializer.data)
