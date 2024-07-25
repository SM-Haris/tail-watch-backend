from decimal import Decimal
from re import T
from django.test import TestCase
import pytest
from history.serializers import HistorySerializer, HistoryCreateSerializer
from tags.models import Tag
from history.models import History
from users.models import CustomUser


@pytest.mark.django_db
class TestHistorySerializers(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser",
            password="12345",
            email="test@gmail.com",
            address="test-address",
            phone_number="12345678",
        )

        self.tag = Tag.objects.create(
            owner=self.user,
            pet_name="Buddy",
            gender="Male",
            disease="None",
            recommended_medicine="None",
            subscription_id="sub_12345",
            delivery_address="123 Street",
            subscription_choice="Monthly",
        )

    def test_history_serializer(self):
        history = History.objects.create(
            tag=self.tag,
            longitude=12.3456789,
            latitude=98.7654321,
        )
        serializer = HistorySerializer(history)
        data = serializer.data
        assert data["id"] == str(history.id)
        assert data["tag"] == self.tag.id
        assert data["longitude"] == "12.3456789"
        assert data["latitude"] == "98.7654321"
        assert data["address"] == history.address

    def test_history_create_serializer(self):
        data = {
            "tag": self.tag.id,
            "longitude": "12.3456789",
            "latitude": "98.7654321",
        }
        serializer = HistoryCreateSerializer(data=data)
        assert serializer.is_valid()
        history = serializer.save()
        assert history.id is not None
        assert history.tag == self.tag
        assert history.longitude == Decimal("12.3456789")
        assert history.latitude == Decimal("98.7654321")
        assert history.address is not None
