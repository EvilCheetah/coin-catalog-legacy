from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/catalog/', include('coin_catalog.urls')),
    path('api/accounts/', include('accounts.api.urls'))
]
