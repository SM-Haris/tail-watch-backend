from rest_framework import serializers
from .validators import validate_password
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator


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
    subscription_id = serializers.EmailField(
        write_only=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    class Meta:
        model = CustomUser
        fields = ["id", "username", "phone_number", "email", "password", "address"]

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data["username"],
            phone_number=validated_data["phone_number"],
            email=validated_data["email"],
            address=validated_data["address"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class CustomUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "phone_number", "email", "address"]


class CustomUserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password], required=False)

    class Meta:
        model = CustomUser
        fields = ["phone_number", "address", "password"]

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address = validated_data.get('address', instance.address)

        if password:
            instance.set_password(password) 
        instance.save()
        
        return instance

