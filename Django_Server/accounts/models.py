from django.db import models

from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser
)

from django.utils import timezone


class User(AbstractBaseUser):
    username = models.CharField(max_length = 255, unique = True)
    email    = models.EmailField(max_length = 255, unique = True)

    #Plan-based account types
    basic_plan    = models.BooleanField(
        default   = True,
        help_text = ("User have the access to the most of the coins in Database. "
                    "No access to price history.")
    )

    advanced_plan = models.BooleanField(
        default   = False,
        help_text = ("User have access to all coins. "
                     "Also have access to price history.")
    )

    business_plan = models.BooleanField(
        default   = False,
        help_text = ("Advanced plan is included. "
                     "Also grants the access to the API.")
    )

    #User Role
    is_active   = models.BooleanField(
        default   = True,
        help_text = ("Designated whether user is active. "
                     "Set to false instead of deleting the account.")
    )

    is_staff    = models.BooleanField(
        default   = False,
        help_text = ("Designated whether user can ADD/EDIT/DELETE coins.")
    )

    is_admin    = models.BooleanField(
        default = False,
        help_text = ("Designated whether user is admin. "
                     "Can nominate roles to other users.")
    )

    date_joined = models.DateTimeField(default = timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
