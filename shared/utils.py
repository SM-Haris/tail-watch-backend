from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed


def ExtractUserFromRequest(request):
    if request.user and request.user.is_superuser:
        return request.user

    jwt_auth = JWTAuthentication()

    try:
        auth_result = jwt_auth.authenticate(request)

        if auth_result is None:
            user = None
        else:
            user, _ = auth_result

        return user
    except AuthenticationFailed:
        return None
