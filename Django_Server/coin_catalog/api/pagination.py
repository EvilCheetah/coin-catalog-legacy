from rest_framework.pagination import (
    PageNumberPagination
)


class StandardResultsSetPagination(PageNumberPagination):
    page_size               = 10
    max_page_size           = 1000
    page_size_query_param   = 'page_size'


class InformationResultsSetPagination(PageNumberPagination):
    """
        Default pagination class for the ViewSets that
        don't "render" additional information
    """
    page_size               = 50
    max_page_size           = 10000
    page_size_query_param   = 'page_size'


class FullInformationResultsSetPagination(PageNumberPagination):
    """
        Pagination class for the 'FullInfoCoinViewSet'
        limits the number of coin in order to ease the
        server
    """
    page_size               = 10
    max_page_size           = 100
    page_size_query_param   = 'page_size'
