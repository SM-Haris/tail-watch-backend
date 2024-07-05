from rest_framework import serializers
from tags.models import Tag
from users.models import CustomUser


class AdminUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["id", "username", "phone_number", "email", "password", "address"]


class AdminTagSerializer(serializers.ModelSerializer):
    qr_code = serializers.CharField(read_only=True)

    class Meta:
        model = Tag
        fields = [
            "pk",
            "owner",
            "pet_name",
            "gender",
            "disease",
            "recommended_medicine",
            "qr_code",
            "subscription_choice",
            "subscription_id",
            "delivery_address",
            "created_at",
        ]
