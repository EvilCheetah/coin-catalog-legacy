import coin_price_history.models as PriceHistoryModel


def get_platform_queryset(request):
     queryset = PriceHistoryModel.Platform.objects.all()

     return queryset


def get_grade_queryset(request):
     queryset = PriceHistoryModel.Grade.objects.all()

     return queryset
