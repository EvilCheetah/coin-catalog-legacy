from django.urls import path, include
from rest_framework import routers

from coin_price_history.api import views

router  = routers.DefaultRouter()

router.register('platform', views.PlatformViewSet, basename = 'platform-model')
router.register('grade',    views.GradeViewSet,    basename = 'grade-model')

urlpatterns = [
    path('', include(router.urls)),
]
