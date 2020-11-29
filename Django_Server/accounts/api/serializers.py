from rest_framework import serializers

from accounts.models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id',          'email',    'username',
                  'is_active',   'is_staff', 'is_admin', 'is_superuser',
                  'date_joined', 'last_login']
