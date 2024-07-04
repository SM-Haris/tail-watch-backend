from urllib import request
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

from shared.utils import ExtractUserFromRequest


class UserObjectMixin:

    def get_object(self):
        jwt_auth = JWTAuthentication()

        try:
            auth_result = jwt_auth.authenticate(self.request)
            if auth_result is None:
                user = None
            else:
                user, _ = auth_result
        except AuthenticationFailed:
            user = None

        if self.request.user.is_superuser:
            return self.request.user

        return user


class UserQuerySetMixin:
    user_field = "name"

    def get_queryset(self, *args, **kwargs):
        user = ExtractUserFromRequest(self.request)

        if not user:
            return []

        queryset = super().get_queryset(*args, **kwargs)

        if user and user.is_superuser:
            return queryset

        self.request.user = user
        return [user]
