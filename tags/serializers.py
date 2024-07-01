from rest_framework import serializers
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "pk",
            "pet_name",
            "gender",
            "disease",
            "recommended_medicine",
            "qr_code",
            "created_at",
        ]
