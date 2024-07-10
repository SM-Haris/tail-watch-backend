from rest_framework import serializers
from .models import History

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['id', 'tag', 'created_at', 'longitude', 'latitude', 'address']

class HistoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['tag', 'longitude', 'latitude']
