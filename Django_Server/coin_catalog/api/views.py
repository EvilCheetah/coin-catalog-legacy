from django.shortcuts import get_object_or_404

#REST imports
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from accounts.permissions import (
    IsAuthenticated,
    IsStaffUser,
    IsAdminUser
)

#Model Imports
import coin_catalog.models as CoinModel

#Serializer Imports
import coin_catalog.api.serializers.list_serializers as CoinListSerializer
import coin_catalog.api.serializers.instance_serializers as CoinInstanceSerializer

#Services Imports
import coin_catalog.services.view_logic.instance_logic as Instance
import coin_catalog.services.view_logic.list_logic as List
import coin_catalog.services.view_logic.post_logic as Post


class BaseModelViewSet(viewsets.ModelViewSet):
    """
        BaseModelViewSet is created for the permission purposes,
        in order to clutter up the ViewSets with 'get_permissions'
        method and set general permission for each method in ViewSet

        Methods:
            - 'create'      - Staff Users only
            - 'list'        - Authenticated Users only
            - 'retrieve'    - Authenticated Users only
            - 'update'      - Staff Users only
            - 'destroy'     - Admin Users only
    """
    permission_classes_by_action = {
        'create':   [IsStaffUser],
        'list':     [IsAuthenticated],
        'retrieve': [IsAuthenticated],
        'update':   [IsStaffUser],
        'destroy':  [IsAdminUser],
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

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_region_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset   = List.get_region_queryset(request)
        serializer = CoinListSerializer.RegionSerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.Region.objects.all()
        region     = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.RegionSerializer(region)
        return Response(serializer.data)


class CountryViewSet(BaseModelViewSet):
    queryset         = CoinModel.Country.objects.all()
    serializer_class = CoinListSerializer.CountrySerializer

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_country_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset   = List.get_country_queryset(request)
        serializer = CoinListSerializer.CountrySerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.Country.objects.all()
        country    = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.CountrySerializer(country)
        return Response(serializer.data)


class CategoryViewSet(BaseModelViewSet):
    queryset         = CoinModel.Category.objects.all()
    serializer_class = CoinListSerializer.CategorySerializer

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_category_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset   = List.get_category_queryset(request)
        serializer = CoinListSerializer.CategorySerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.Category.objects.all()
        category   = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.CategorySerializer(category)
        return Response(serializer.data)


class CollectionViewSet(BaseModelViewSet):
    queryset         = CoinModel.Collection.objects.all()
    serializer_class = CoinListSerializer.CollectionSerializer

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_collection_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset   = List.get_collection_queryset(request)
        serializer = CoinListSerializer.CollectionSerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.Collection.objects.all()
        collection = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.CollectionSerializer(collection)
        return Response(serializer.data)


class CurrencyViewSet(BaseModelViewSet):
    queryset         = CoinModel.Currency.objects.all()
    serializer_class = CoinListSerializer.CurrencySerializer

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_currency_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset   = List.get_currency_queryset(request)
        serializer = CoinListSerializer.CurrencySerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset = CoinModel.Currency.objects.all()
        currency = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.CurrencySerializer(currency)
        return Response(serializer.data)


class CountryCurrencyViewSet(BaseModelViewSet):
    queryset         = CoinModel.CountryCurrency.objects.all()
    serializer_class = CoinListSerializer.CountryCurrencySerializer

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_country_currency_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset   = List.get_country_currency_queryset(request)
        serializer = CoinListSerializer.CountryCurrencySerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset         = CoinModel.CountryCurrency.objects.all()
        country_currency = get_object_or_404(queryset, pk = pk)
        serializer       = CoinInstanceSerializer.CountryCurrencySerializer(country_currency)
        return Response(serializer.data)


class MintedByViewSet(BaseModelViewSet):
    queryset         = CoinModel.MintedBy.objects.all()
    serializer_class = CoinListSerializer.MintedBySerializer

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_minted_by_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset   = List.get_minted_by_queryset(request)
        serializer = CoinListSerializer.MintedBySerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.MintedBy.objects.all()
        minted_by  = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.MintedBySerializer(minted_by)
        return Response(serializer.data)


class DesignerNameViewSet(BaseModelViewSet):
    queryset         = CoinModel.DesignerName.objects.all()
    serializer_class = CoinListSerializer.DesignerNameSerializer

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_designer_name_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset   = List.get_designer_name_queryset(request)
        serializer = CoinListSerializer.DesignerNameSerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset      = CoinModel.DesignerName.objects.all()
        designer_name = get_object_or_404(queryset, pk = pk)
        serializer    = CoinInstanceSerializer.DesignerNameSerializer(designer_name)
        return Response(serializer.data)


class SculptorNameViewSet(BaseModelViewSet):
    queryset         = CoinModel.SculptorName.objects.all()
    serializer_class = CoinListSerializer.SculptorNameSerializer

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_sculptor_name_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset   = List.get_sculptor_name_queryset(request)
        serializer = CoinListSerializer.SculptorNameSerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset      = CoinModel.SculptorName.objects.all()
        sculptor_name = get_object_or_404(queryset, pk = pk)
        serializer    = CoinInstanceSerializer.SculptorNameSerializer(sculptor_name)
        return Response(serializer.data)


class MaterialViewSet(BaseModelViewSet):
    queryset         = CoinModel.Material.objects.all()
    serializer_class = CoinListSerializer.MaterialSerializer

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_material_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset   = List.get_material_queryset(request)
        serializer = CoinListSerializer.MaterialSerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.Material.objects.all()
        material   = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.MaterialSerializer(material)
        return Response(serializer.data)


class QualityViewSet(BaseModelViewSet):
    queryset         = CoinModel.Quality.objects.all()
    serializer_class = CoinListSerializer.QualitySerializer

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_quality_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset   = List.get_quality_queryset(request)
        serializer = CoinListSerializer.QualitySerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.Quality.objects.all()
        qualtity   = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.QualitySerializer(qualtity)
        return Response(serializer.data)


class EdgeViewSet(BaseModelViewSet):
    queryset         = CoinModel.Edge.objects.all()
    serializer_class = CoinListSerializer.EdgeSerializer

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_edge_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset   = List.get_edge_queryset(request)
        serializer = CoinListSerializer.EdgeSerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.Edge.objects.all()
        edge       = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.EdgeSerializer(edge)
        return Response(serializer.data)


class ShapeViewSet(BaseModelViewSet):
    queryset         = CoinModel.Shape.objects.all()
    serializer_class = CoinListSerializer.ShapeSerializer

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_shape_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset   = List.get_shape_queryset(request)
        serializer = CoinListSerializer.ShapeSerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.Shape.objects.all()
        shape      = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.ShapeSerializer(edge)
        return Response(serializer.data)


class CoinFamilyViewSet(BaseModelViewSet):
    queryset         = CoinModel.CoinFamily.objects.all()
    serializer_class = CoinListSerializer.CoinFamilySerializer

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_coin_family_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset   = List.get_coin_family_queryset(request)
        serializer = CoinListSerializer.CoinFamilySerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset    = CoinModel.CoinFamily.objects.all()
        coin_family = get_object_or_404(queryset, pk = pk)
        serializer  = CoinInstanceSerializer.CountrySerializer(coin_family)
        return Response(serializer.data)


class CoinStyleViewSet(BaseModelViewSet):
    queryset         = CoinModel.CoinStyle.objects.all()
    serializer_class = CoinListSerializer.CoinStyleSerializer

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_coin_style_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset = List.get_coin_style_queryset(request)
        serializer = CoinListSerializer.CoinStyleSerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.CoinStyle.objects.all()
        coin_style = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.CoinStyleSerializer(coin_style)
        return Response(serializer.data)


class SubStyleViewSet(BaseModelViewSet):
    queryset         = CoinModel.SubStyle.objects.all()
    serializer_class = CoinListSerializer.SubStyleSerializer

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_sub_style_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset   = List.get_sub_style_queryset(request)
        serializer = CoinListSerializer.SubStyleSerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.SubStyle.objects.all()
        sub_style  = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.SubStyleSerializer(sub_style)
        return Response(serializer.data)


class NoteViewSet(BaseModelViewSet):
    queryset         = CoinModel.Note.objects.all()
    serializer_class = CoinListSerializer.NoteSerializer

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_note_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset   = List.get_note_queryset(request)
        serializer = CoinListSerializer.NoteSerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.Note.objects.all()
        note       = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.NoteSerializer(note)
        return Response(serializer.data)


class SideOfCoinViewSet(BaseModelViewSet):
    queryset         = CoinModel.SideOfCoin.objects.all()
    serializer_class = CoinListSerializer.SideOfCoinSerializer

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_side_of_coin_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset   = List.get_side_of_coin_queryset(request)
        serializer = CoinListSerializer.SideOfCoinSerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset     = CoinModel.SideOfCoin.objects.all()
        side_of_coin = get_object_or_404(queryset, pk = pk)
        serializer   = CoinInstanceSerializer.SideOfCoinSerializer(side_of_coin)
        return Response(serializer.data)


class CoinDesignerViewSet(BaseModelViewSet):
    queryset         = CoinModel.CoinDesigner.objects.all()
    serializer_class = CoinListSerializer.CoinAllDesignersSerializer

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_coin_designer_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset   = List.get_coin_designer_queryset(request)
        serializer = CoinListSerializer.CoinAllDesignersSerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.CoinDesigner.objects.all()
        designer   = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.CoinAllDesignersSerializer(designer)
        return Response(serializer.data)


class CoinSculptorViewSet(BaseModelViewSet):
    queryset         = CoinModel.CoinSculptor.objects.all()
    serializer_class = CoinListSerializer.CoinAllSculptorsSerializer

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_coin_sculptor_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset   = List.get_coin_sculptor_queryset(request)
        serializer = CoinListSerializer.CoinAllSculptorsSerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = CoinModel.CoinSculptor.objects.all()
        sculptor   = get_object_or_404(queryset, pk = pk)
        serializer = CoinInstanceSerializer.CoinAllSculptorsSerializer(sculptor)
        return Response(serializer.data)

class ImageViewSet(BaseModelViewSet):
    queryset         = CoinModel.Image.objects.all()
    serializer_class = CoinListSerializer.ImageSerializer

    def create(self, request):
        response_data, status = Post.get_response_for_post_request_for_image_viewset(request)
        return Response(response_data, status = status)

    def list(self, request):
        queryset   = List.get_image_queryset(self.request)
        serializer = CoinListSerializer.ImageSerializer(queryset, many = True)
        return Response(serializer.data)

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
    queryset         = CoinModel.CoinStyle.objects.all()
    #Has the same serializer for Instance and List
    serializer_class = CoinInstanceSerializer.FullInfoCoinSerializer

    def get_queryset(self):
        return List.get_full_info_coin_queryset(self.request)

    def retrieve(self, request, pk = None):
        queryset    = CoinModel.CoinStyle.objects.all()
        coin_style  = get_object_or_404(queryset, pk = pk)
        serializer  = CoinInstanceSerializer.FullInfoCoinSerializer(coin_style)
        return Response(serializer.data)
