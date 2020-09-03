from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from catalog.models import CoinStyle
from catalog.api.serializers import CoinSerializer


@api_view(['GET'])
def api_coin_list(request):
    try:
        coin = CoinStyle.objects.all()

    except CoinStyle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CoinSerializer(coin, many=True)
    return Response(serializer.data)
