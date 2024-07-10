from random import choices
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from tags.validators import validate_subscription_choice
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    subscription_choice = serializers.CharField(
        write_only=True, validators=[validate_subscription_choice]
    )
    subscription_id = serializers.CharField(
        write_only=True, validators=[UniqueValidator(queryset=Tag.objects.all())]
    )
    delivery_address = serializers.CharField(write_only=True)

    class Meta:
        model = Tag
        fields = [
            "pk",
            "pet_name",
            "gender",
            "disease",
            "recommended_medicine",
            "subscription_choice",
            "subscription_id",
            "delivery_address",
            "created_at",
        ]


class TagUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "pet_name",
            "gender",
            "disease",
            "recommended_medicine",
        ]

class TagTrackSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.username')
    owner_address = serializers.CharField(source='owner.address')
    owner_phone_number = serializers.CharField(source='owner.phone_number')

    class Meta:
        model = Tag
        fields = [
            "id",
            "pet_name",
            "gender",
            "disease",
            "recommended_medicine",
            "subscription_choice",
            "subscription_id",
            "delivery_address",
            "created_at",
            "owner_name",
            "owner_address",
            "owner_phone_number",
        ]