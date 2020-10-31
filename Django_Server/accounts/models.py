from django.db import models

from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser
)


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password = None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
                email    = self.normalize_email(email),
                username = username
        )

        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, email, username, password = None):
        user = self.create_user(
                email    = self.normalize_email(email),
                username = username,
                password = password
        )

        user.is_staff     = True
        user.is_admin     = True
        user.is_superuser = True

        user.save(using = self._db)

        return user


class Account(AbstractBaseUser):
    email    = models.EmailField(max_length = 255, unique = True)
    username = models.CharField(max_length = 255, unique = True)

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

    is_superuser = models.BooleanField(
        default = False,
        help_text = ("Designated whether user is the owner of the site. "
                     "Can nominate admins.")
    )

    date_joined = models.DateTimeField(auto_now_add = True)
    last_login  = models.DateTimeField(auto_now = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj = None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
