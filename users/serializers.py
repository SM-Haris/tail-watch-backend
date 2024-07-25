from rest_framework import serializers

from users.util import send_password_reset_email
from .validators import validate_jwt_token, validate_password, validate_user_email, validate_user_id
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        user_data = {}

        user_data["id"] = self.user.id
        user_data["username"] = self.user.username
        user_data["email"] = self.user.email
        user_data["phone_number"] = self.user.phone_number
        user_data["address"] = self.user.address

        data["user"] = user_data

        return data


class CustomUserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    class Meta:
        model = CustomUser
        fields = ["id", "username", "phone_number", "email", "password", "address"]

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data.get("username"),
            phone_number=validated_data.get("phone_number"),
            email=validated_data.get("email"),
            address=validated_data.get("address"),
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class CustomUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "phone_number", "email", "address"]


class CustomUserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, validators=[validate_password], required=False
    )

    class Meta:
        model = CustomUser
        fields = ["phone_number", "address", "password"]

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        instance.phone_number = validated_data.get("phone_number", instance.phone_number)
        instance.address = validated_data.get("address", instance.address)

        if password:
            instance.set_password(password)
        instance.save()

        return instance

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[validate_user_email])

    def save(self):
        user = CustomUser.objects.get(email=self.validated_data['email'])
        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)

        send_password_reset_email(user,token)

class PasswordResetSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, validators=[validate_password])
    uid = serializers.CharField(validators=[validate_user_id])
    token = serializers.CharField()

    def validate(self, attrs):
        token = attrs.get('token')
        uid = attrs.get('uid')
        validate_jwt_token(token,uid)

        return attrs

    def save(self):
        uid = (self.validated_data['uid'])
        user = CustomUser.objects.get(pk=uid)
        user.set_password(self.validated_data['new_password'])
        user.save()