from urllib import request
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed


class UserQuerySetMixin:
    user_field = "owner"

    def get_queryset(self, *args, **kwargs):
        jwt_auth = JWTAuthentication()

        try:
            auth_result = jwt_auth.authenticate(self.request)
            if auth_result is None:
                user = None
            else:
                user, _ = auth_result
        except AuthenticationFailed:
            user = None

        lookup_data = {}

        lookup_data[self.user_field] = user

        queryset = super().get_queryset(*args, **kwargs)
        if self.request.user.is_superuser:
            return queryset
        

        self.request.user = user
        return queryset.filter(**lookup_data)
