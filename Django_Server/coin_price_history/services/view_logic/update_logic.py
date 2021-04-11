import coin_price_history.models as CoinPriceHistory
from coin_price_history.api import serializers

from coin_catalog.services.view_logic.update_logic import (
    _get_response_data
)

class PlatformUpdateRequest:
    """
    This class is designated for
        - Model:   Platform
        - Viewset: PlatformViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinPriceHistory.Platform.objects.all(),
            serializer_class    = serializers.PlatformSerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )


class GradeUpdateRequest:
    """
    This class is designated for
        - Model:   Grade
        - Viewset: GradeViewSet
    """
    def get_response(primary_key, request, partial = False):
        return _get_response_data(
            queryset            = CoinPriceHistory.Grade.objects.all(),
            serializer_class    = serializers.GradeSerializer,
            request             = request,
            primary_key         = primary_key,
            partial             = partial
        )
