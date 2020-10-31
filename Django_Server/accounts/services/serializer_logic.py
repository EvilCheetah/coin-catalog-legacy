from rest_framework import serializers


def raise_error_if_passwords_do_not_match(password1: str, password2: str):
    """
    Used by AccountSerializer to check if passwords in form match
    If not raises the error
    """
    if ( password1 != password2 ):
        raise serializers.ValidationError(
            {
                'password': 'Passwords must match.'
            }
        )
