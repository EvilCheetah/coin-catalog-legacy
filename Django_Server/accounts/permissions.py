from rest_framework.permissions import BasePermission


class AllowAny(BasePermission):
    """
        Allow any access.
    """
    def has_permission(self, request, view):
        return True


class IsAuthenticated(BasePermission):
    """
        Allow access only to authenticated users that are not banned.
    """
    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False

        return bool(
            request.user.is_active
        )


class IsStaffUser(BasePermission):
    """
        Allow access only to staff members.
            - Is superuser
            OR
            - Not banned 'is_staff' or 'is_admin'

    """
    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False

        return bool(
            request.user.is_superuser or
            (
                (request.user.is_staff or request.user.is_admin) and
                request.user.is_active
            )
        )


class IsAdminUser(BasePermission):
    """
        Allow access only to admins.
            - Is superuser
            OR
            - Not banned 'is_admin'
    """
    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False

        return bool(
            request.user.is_superuser or
            (request.user.is_admin and request.user.is_active)
        )


class IsSuperUser(BasePermission):
    """
        Allow access only to superuser
    """
    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False

        return bool(
            request.user.is_superuser
        )
