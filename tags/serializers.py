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