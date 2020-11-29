from django.urls import path, include
from rest_framework import routers

from accounts.api import views


router = routers.DefaultRouter()

router.register('accounts', views.UserViewSet, basename = 'user-view-set')


urlpatterns = [
    path('', include(router.urls)),
]
