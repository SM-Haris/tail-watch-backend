from unittest import TestCase
import pytest
from django.utils import timezone
from tags.models import Tag
from history.models import History
import uuid

from users.models import CustomUser


@pytest.mark.django_db
class TestHistoryModel(TestCase):
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

    def test_history_model(self):
        history = History.objects.create(
            tag=self.tag,
            longitude=12.3456789,
            latitude=98.7654321,
        )
        assert history.id is not None
        assert history.tag == self.tag
        assert history.created_at <= timezone.now()
        assert history.longitude == 12.3456789
        assert history.latitude == 98.7654321
        assert history.address is not None
        assert str(history) == f"History for Tag {self.tag.id} at {history.created_at}"
