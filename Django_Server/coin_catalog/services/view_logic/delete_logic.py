from django.shortcuts import get_object_or_404

from rest_framework import status

from coin_catalog import models as CoinModel


def _success_delete():
    """
        Returns successful response when object is deleted
    """
    response_data = {'status': 'Object was successfully deleted'}
    return response_data, status.HTTP_200_OK


def _failure_delete():
    """
        Returns 'Internal Error' when wasn't able to delete object
    """
    response_data = {'status': 'Could not delete object... Try again or contact support'}
    return response_data, status.HTTP_500_INTERNAL_SERVER_ERROR


def _delete_object(queryset, primary_key):
    """
        Generalized function for deleting the object
    """
    object    = get_object_or_404(queryset, pk = primary_key)
    operation = object.delete()

    if operation:
        return _success_delete()
    else:
        return _failure_delete()


class RegionDeleteRequest:
    """
    This class is designated for
        - Model:   Region
        - Viewset: RegionViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.Region.objects.all(),
            primary_key =  primary_key
        )


class CountryDeleteRequest:
    """
    This class is designated for
        - Model:   Country
        - Viewset: CountryViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.Country.objects.all(),
            primary_key =  primary_key
        )


class CategoryDeleteRequest:
    """
    This class is designated for
        - Model:   Category
        - Viewset: CategoryViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.Category.objects.all(),
            primary_key =  primary_key
        )


class CollectionDeleteRequest:
    """
    This class is designated for
        - Model:   Collection
        - Viewset: CollectionViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.Collection.objects.all(),
            primary_key =  primary_key
        )


class CurrencyDeleteRequest:
    """
    This class is designated for
        - Model:   Currency
        - Viewset: CurrencyViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.Currency.objects.all(),
            primary_key =  primary_key
        )


class CountryCurrencyDeleteRequest:
    """
    This class is designated for
        - Model:   CountryCurrency
        - Viewset: CountryCurrencyViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.CountryCurrency.objects.all(),
            primary_key =  primary_key
        )


class MintedByDeleteRequest:
    """
    This class is designated for
        - Model:   MintedBy
        - Viewset: MintedByViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.MintedBy.objects.all(),
            primary_key =  primary_key
        )


class DesignerNameDeleteRequest:
    """
    This class is designated for
        - Model:   DesignerName
        - Viewset: DesignerNameViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.DesignerName.objects.all(),
            primary_key =  primary_key
        )


class SculptorNameDeleteRequest:
    """
    This class is designated for
        - Model:   SculptorName
        - Viewset: SculptorNameViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.SculptorName.objects.all(),
            primary_key =  primary_key
        )


class MaterialDeleteRequest:
    """
    This class is designated for
        - Model:   Material
        - Viewset: MaterialViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.Material.objects.all(),
            primary_key =  primary_key
        )


class QualityDeleteRequest:
    """
    This class is designated for
        - Model:   Quality
        - Viewset: QualityViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.Quality.objects.all(),
            primary_key =  primary_key
        )


class EdgeDeleteRequest:
    """
    This class is designated for
        - Model:   Edge
        - Viewset: EdgeViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.Edge.objects.all(),
            primary_key =  primary_key
        )


class ShapeDeleteRequest:
    """
    This class is designated for
        - Model:   Shape
        - Viewset: ShapeViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.Shape.objects.all(),
            primary_key =  primary_key
        )


class CoinFamilyDeleteRequest:
    """
    This class is designated for
        - Model:   CoinFamily
        - Viewset: CoinFamilyViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.CoinFamily.objects.all(),
            primary_key =  primary_key
        )


class CoinStyleDeleteRequest:
    """
    This class is designated for
        - Model:   CoinStyle
        - Viewset: CoinStyleViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.CoinStyle.objects.all(),
            primary_key =  primary_key
        )


class SubStyleDeleteRequest:
    """
    This class is designated for
        - Model:   SubStyle
        - Viewset: SubStyleViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.SubStyle.objects.all(),
            primary_key =  primary_key
        )


class NoteDeleteRequest:
    """
    This class is designated for
        - Model:   Note
        - Viewset: NoteViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.Note.objects.all(),
            primary_key =  primary_key
        )


class SideOfCoinDeleteRequest:
    """
    This class is designated for
        - Model:   SideOfCoin
        - Viewset: SideOfCoinViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.SideOfCoin.objects.all(),
            primary_key =  primary_key
        )


class CoinDesignerDeleteRequest:
    """
    This class is designated for
        - Model:   CoinDesigner
        - Viewset: CoinDesignerViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.CoinDesigner.objects.all(),
            primary_key =  primary_key
        )


class CoinSculptorDeleteRequest:
    """
    This class is designated for
        - Model:   CoinSculptor
        - Viewset: CoinSculptorViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.CoinSculptor.objects.all(),
            primary_key =  primary_key
        )


class ImageDeleteRequest:
    """
    This class is designated for
        - Model:   Image
        - Viewset: ImageViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinModel.Image.objects.all(),
            primary_key =  primary_key
        )
