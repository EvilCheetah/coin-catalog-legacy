from django.shortcuts import get_object_or_404

from rest_framework import status

import coin_catalog.models as CoinModel
import coin_catalog.api.serializers.list_serializers as serializers

def _success_update(serializer):
    """
        Returns the serialized 'response_data' and 'status'-code
        When objects is Updated
    """
    response_data = serializer.data
    response_data['status'] = "Successfully Updated"
    return response_data, status.HTTP_200_OK


def _get_response_data(queryset, serializer_class, request, primary_key, partial):
    """
        Generalized function for update
    """
    object = get_object_or_404(queryset, pk = primary_key)

    serializer = serializer_class(object, data = request.data, partial = partial)
    serializer.is_valid(raise_exception = True)

    serializer.save()
    return _success_update(serializer)


class RegionUpdateRequest:
    """
    This class is designated for
        - Model:   Region
        - Viewset: RegionViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.Region.objects.all(),
            serializer_class    = serializers.RegionSerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class CountryUpdateRequest:
    """
    This class is designated for
        - Model:   Country
        - Viewset: CountryViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.Country.objects.all(),
            serializer_class    = serializers.CountrySerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class CategoryUpdateRequest:
    """
    This class is designated for
        - Model:   Category
        - Viewset: CategoryViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.Category.objects.all(),
            serializer_class    = serializers.CategorySerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class CollectionUpdateRequest:
    """
    This class is designated for
        - Model:   Collection
        - Viewset: CollectionViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.Collection.objects.all(),
            serializer_class    = serializers.CollectionSerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class CurrencyUpdateRequest:
    """
    This class is designated for
        - Model:   Currency
        - Viewset: CurrencyViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.Currency.objects.all(),
            serializer_class    = serializers.CurrencySerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class CountryCurrencyUpdateRequest:
    """
    This class is designated for
        - Model:   CountryCurrency
        - Viewset: CountryCurrencyViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.CountryCurrency.objects.all(),
            serializer_class    = serializers.CountryCurrencySerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class MintedByUpdateRequest:
    """
    This class is designated for
        - Model:   MintedBy
        - Viewset: MintedByViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.MintedBy.objects.all(),
            serializer_class    = serializers.MintedBySerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class DesignerNameUpdateRequest:
    """
    This class is designated for
        - Model:   DesignerName
        - Viewset: DesignerNameViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.DesignerName.objects.all(),
            serializer_class    = serializers.DesignerNameSerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class SculptorNameUpdateRequest:
    """
    This class is designated for
        - Model:   SculptorName
        - Viewset: SculptorNameViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.SculptorName.objects.all(),
            serializer_class    = serializers.SculptorNameSerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class MaterialUpdateRequest:
    """
    This class is designated for
        - Model:   Material
        - Viewset: MaterialViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.Material.objects.all(),
            serializer_class    = serializers.MaterialSerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class QualityUpdateRequest:
    """
    This class is designated for
        - Model:   Quality
        - Viewset: QualityViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.Quality.objects.all(),
            serializer_class    = serializers.QualitySerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class EdgeUpdateRequest:
    """
    This class is designated for
        - Model:   Edge
        - Viewset: EdgeViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.Edge.objects.all(),
            serializer_class    = serializers.EdgeSerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class ShapeUpdateRequest:
    """
    This class is designated for
        - Model:   Shape
        - Viewset: ShapeViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.Shape.objects.all(),
            serializer_class    = serializers.ShapeSerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class CoinFamilyUpdateRequest:
    """
    This class is designated for
        - Model:   CoinFamily
        - Viewset: CoinFamilyViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.CoinFamily.objects.all(),
            serializer_class    = serializers.CoinFamilySerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class CoinStyleUpdateRequest:
    """
    This class is designated for
        - Model:   CoinStyle
        - Viewset: CoinStyleViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.CoinStyle.objects.all(),
            serializer_class    = serializers.CoinStyleSerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class SubStyleUpdateRequest:
    """
    This class is designated for
        - Model:   SubStyle
        - Viewset: SubStyleViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.SubStyle.objects.all(),
            serializer_class    = serializers.SubStyleSerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class NoteUpdateRequest:
    """
    This class is designated for
        - Model:   Note
        - Viewset: NoteViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.Note.objects.all(),
            serializer_class    = serializers.NoteSerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class SideOfCoinUpdateRequest:
    """
    This class is designated for
        - Model:   SideOfCoin
        - Viewset: SideOfCoinViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.SideOfCoin.objects.all(),
            serializer_class    = serializers.SideOfCoinSerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class CoinDesignerUpdateRequest:
    """
    This class is designated for
        - Model:   CoinDesigner
        - Viewset: CoinDesignerViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.CoinDesigner.objects.all(),
            serializer_class    = serializers.CoinDesignerSerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class CoinSculptorUpdateRequest:
    """
    This class is designated for
        - Model:   CoinSculptor
        - Viewset: CoinSculptorViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.CoinSculptor.objects.all(),
            serializer_class    = serializers.CoinSculptorSerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class ImageUpdateRequest:
    """
    This class is designated for
        - Model:   Image
        - Viewset: ImageViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinModel.Image.objects.all(),
            serializer_class    = serializers.ImageSerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )
