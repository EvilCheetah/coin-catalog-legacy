from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('admin/',       admin.site.urls),
    path('api/catalog/', include('coin_catalog.urls')),
    #path('api/history/', include('coin_price_history.urls')),

    path('auth/',        include('djoser.urls')),
    path('auth/',        include('djoser.urls.jwt')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += [path('api-auth/',    include('rest_framework.urls'))]
