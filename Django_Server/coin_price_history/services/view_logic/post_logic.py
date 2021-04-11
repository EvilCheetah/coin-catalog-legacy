from coin_price_history.api import serializers
import coin_price_history.models as CoinPriceHistory

from coin_catalog.services.view_logic.post_logic import (
    _success_create,
    _success_find
)

class PlatformPostRequest:
    """
    This class is designated for
        - Model:   Platform
        - Viewset: PlatformViewSet
    """
    def get_response(request):
        serializer = serializers.PlatformSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        platform   = CoinPriceHistory.Platform.objects.filter(
                name__iexact = serializer.validated_data['name']
                )

        if platform:
            serializer = serializers.PlatformSerializer(region.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)


class GradePostRequest:
    """
    This class is designated for
        - Model:   Grade
        - Viewset: GradeViewSet
    """
    def get_response(request):
        serializer = serializers.GradeSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        grade      = CoinPriceHistory.Grade.objects.filter(
                abbreviation__iexact = serializer.validated_data['abbreviation']
                )

        if grade:
            serializer = serializers.GradeSerializer(region.first())
            return _success_find(serializer)

        serializer.save()
        return _success_create(serializer)
