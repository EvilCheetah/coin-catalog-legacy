def _get_serialized_data(primary_key, model_, serializer_, request):

    context = {'request': request}
    queryset = model_.objects.filter(pk = primary_key)
    serializer = serializer_(queryset, many = True, context = context)
    return serializer.data
