from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from accounts import models as AccountModel
from accounts.api import serializers as AccountSerializer
from accounts.services import view_logic as ViewLogic


@api_view(['POST'])
def registration(request):
    serializer = AccountSerializer.RegistrationSerializer(data = request.data)
    data = {}

    if serializer.is_valid():
        account = serializer.save()
        data = ViewLogic.registration_success_response_data(account)

    else:
        data = serializer.errors

    return Response(data)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AccountModel.Account.objects.all()
    serializer_class = AccountSerializer.UserSerializer
