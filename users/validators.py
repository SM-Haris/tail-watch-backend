import re
from django.core.exceptions import ValidationError
from users.models import CustomUser
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken


def validate_password(value):
    if not re.match(
        r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+}{":;\'?><,./\|~\-\\\[\]])[0-9a-zA-Z!@#$%^&*()_+}{":;\'?><,./\|~\-\\\[\]]{8,}$',
        value,
    ):
        raise ValidationError(
            "Password must contain at least 8 characters, including uppercase, lowercase, digits, and special characters."
        )


def validate_user_email(user_email):
    user = CustomUser.objects.get(email=user_email)
    if user is None:
        raise ValidationError("Invalid User email")


def validate_jwt_token(token, user_id):
    try:
        refresh = AccessToken(token)
        if refresh["user_id"] != user_id:
            raise serializers.ValidationError("Invalid Token")
        return refresh
    except Exception as e:
        raise serializers.ValidationError(e)


def validate_user_id(user_id):
    try:
        if not CustomUser.objects.filter(pk=user_id).exists():
            raise serializers.ValidationError("Invalid User ID")
    except Exception as e:
        raise serializers.ValidationError("Invalid User ID")
