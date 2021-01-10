from rest_framework.pagination import (
    PageNumberPagination
)


class StandardResultsSetPagination(PageNumberPagination):
    page_size               = 10
    max_page_size           = 1000
    page_size_query_param   = 'page_size'


class InformationResultsSetPagination(PageNumberPagination):
    page_size               = 25
    max_page_size           = 1000
    page_size_query_param   = 'page_size'
