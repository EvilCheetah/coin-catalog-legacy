from rest_framework.exceptions import APIException


##---------------------Exception Function---------------------##
def type_error_for_list_parameter(filter_field):
    raise APIException(detail = {'success': 'false',
                                 'message': f"'Query Parameter' Error! Expected 'integer' or 'list of integers' in {filter_field} Field"},
                       code = 400)


def type_error_for_integer_range_parameter(filter_field):
    raise APIException(detail = {'success': 'false',
                                 'message': f"'Query Parameter' Error! Expected 'integer' in {filter_field} Field"},
                       code = 400)


def type_error_for_float_range_parameter(filter_field):
    raise APIException(detail = {'success': 'false',
                                 'message': f"'Query Parameter' Error! Expected 'float' in {filter_field} Field"},
                       code = 400)


def type_error_for_integer_parameter(filter_field):
    raise APIException(detail = {'success': 'false',
                                 'message': f"'Query Parameter' Error! Expected 'integer' in {filter_field} Field"},
                       code = 400)


def type_error_for_string_parameter(filter_field):
    raise APIException(detail = {'success': 'false',
                                 'message': f"'Query Parameter' Error! Expected 'string' in {filter_field} Field"},
                       code = 400)
