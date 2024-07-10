from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status

from rest_framework.exceptions import APIException
from rest_framework import status

class ForbiddenException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'User is not present. Token is missing.'
    default_code = 'forbidden'

class UserJWTAuthentication(JWTAuthentication):

    def authenticate(self, request):
        header = self.get_header(request)

        if header is None:
            raise ForbiddenException

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            raise ForbiddenException

        validated_token = self.get_validated_token(raw_token)

        try:
            user = self.get_user(validated_token)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        except AuthenticationFailed as e:
            raise AuthenticationFailed(e.args[0])

        request.user = user
        return (user, validated_token)
