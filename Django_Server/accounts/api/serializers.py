from rest_framework import serializers

from accounts.models import Account
from accounts.services import serializer_logic as Logic


class RegistrationSerializer(serializers.ModelSerializer):
    confirmation_password = serializers.CharField(
        style      = {'input_type': 'password'},
        write_only = True
    )

    class Meta:
        model  = Account
        fields = ['email', 'username', 'password', 'confirmation_password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def save(self):
        account = Account(
            email    = self.validated_data['email'],
            username = self.validated_data['username']
        )

        password              = self.validated_data['password']
        confirmation_password = self.validated_data['confirmation_password']

        Logic.raise_error_if_passwords_do_not_match(password, confirmation_password)

        account.set_password(password)
        account.save()

        return account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email',       'username',
                  'is_active',   'is_staff', 'is_admin', 'is_superuser',
                  'date_joined', 'last_login']
