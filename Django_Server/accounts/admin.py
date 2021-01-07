from django.contrib import admin
from accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display  = ['email', 'username', 'date_joined', 'last_login',
                     'is_active', 'is_staff', 'is_admin', 'is_superuser']
    search_fields = ['email', 'username']


admin.site.register(Account, AccountAdmin)
