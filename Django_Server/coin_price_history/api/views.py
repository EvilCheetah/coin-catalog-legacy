# Django Imports
from django.shortcuts import get_object_or_404

# REST Imports
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

# Model Imports
import coin_price_history.models as PriceHistoryModel

# Serializer Imports
from coin_price_history.api import serializers

# Services Imports
import coin_price_history.services.view_logic.list_logic as List
import coin_price_history.services.view_logic.post_logic as Create
import coin_price_history.services.view_logic.delete_logic as Delete
import coin_price_history.services.view_logic.update_logic as Update

# Pagination Imports
from services.pagination import (
    StandardResultsSetPagination,
    InformationResultsSetPagination,
    FullInformationResultsSetPagination
)


class BaseModelViewSet(viewsets.ModelViewSet):
    """
        BaseModelViewSet is created for:
            1) Handle the requests methods(PUT, POST, PATCH, DELETE)

            2) Permission purposes, in order to clutter up the
                ViewSets with 'get_permissions' method and set
                general permission for each method in ViewSet

        Methods:
            - 'create'          -
            - 'destroy'         -
            - 'list'            -
            - 'partial_update'  -
            - 'retrieve'        -
            - 'update'          -
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

    # NOT READY
    # permission_classes_by_action = {
    #     'create':           [IsStaffUser],
    #     'destroy':          [IsAdminUser],
    #     'list':             [IsAuthenticated],
    #     'partial_update':   [IsStaffUser],
    #     'retrieve':         [IsAuthenticated],
    #     'update':           [IsStaffUser],
    # }
    #
    # def get_permissions(self):
    #     try:
    #         return [permission() for permission in self.permission_classes_by_action[self.action]]
    #     except KeyError:
    #         return [permission() for permission in self.permission_classes]



class PlatformViewSet(BaseModelViewSet):
    queryset         = PriceHistoryModel.Platform.objects.all()
    serializer_class = serializers.PlatformSerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.PlatformPostRequest
    destroy_method        = Delete.PlatformDeleteRequest
    update_method         = Update.PlatformUpdateRequest
    partial_update_method = Update.PlatformUpdateRequest

    def list(self, request):
        queryset   = List.get_platform_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = serializers.PlatformSerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = PriceHistoryModel.Platform.objects.all()
        platform   = get_object_or_404(queryset, pk = pk)
        serializer = serializers.PlatformSerializer(platform)
        return Response(serializer.data)


class GradeViewSet(BaseModelViewSet):
    queryset         = PriceHistoryModel.Grade.objects.all()
    serializer_class = serializers.GradeSerializer
    pagination_class = InformationResultsSetPagination

    create_method         = Create.GradePostRequest
    destroy_method        = Delete.GradeDeleteRequest
    update_method         = Update.GradeUpdateRequest
    partial_update_method = Update.GradeUpdateRequest

    def list(self, request):
        queryset   = List.get_grade_queryset(request)
        page       = self.paginate_queryset(queryset)
        serializer = serializers.GradeSerializer(page, many = True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset   = PriceHistoryModel.Grade.objects.all()
        grade      = get_object_or_404(queryset, pk = pk)
        serializer = serializers.GradeSerializer(platform)
        return Response(serializer.data)
