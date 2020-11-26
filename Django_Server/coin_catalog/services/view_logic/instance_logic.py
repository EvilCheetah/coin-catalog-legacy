from rest_framework.response import Response


def get_object_instance(primary_key, model_, serializer_, request):
    context = {'request': request}
    queryset = model_.objects.filter(pk = primary_key)
    serializer = serializer_(queryset, many = True, context = context)
    return Response(serializer.data)
