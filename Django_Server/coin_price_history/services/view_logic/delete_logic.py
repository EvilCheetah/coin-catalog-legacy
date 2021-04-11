import coin_price_history.models as CoinPriceHistory

from coin_catalog.services.view_logic.delete_logic import (
    _delete_object
)


class PlatformDeleteRequest:
    """
    This class is designated for
        - Model:   Platform
        - Viewset: PlatformViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinPriceHistory.Platform.objects.all(),
            primary_key = primary_key
        )


class GradeDeleteRequest:
    """
    This class is designated for
        - Model:   Grade
        - Viewset: GradeViewSet
    """
    def get_response(primary_key, request):
        return _delete_object(
            queryset    = CoinPriceHistory.Grade.objects.all(),
            primary_key = primary_key
        )
