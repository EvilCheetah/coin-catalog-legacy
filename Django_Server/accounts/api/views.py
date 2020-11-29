from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from accounts import models as AccountModel
from accounts.api import serializers as AccountSerializer
from accounts.services import view_logic as ViewLogic


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AccountModel.Account.objects.all()
    serializer_class = AccountSerializer.UserSerializer
