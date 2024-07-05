# tags/tests/test_serializers.py

import pytest
from rest_framework.test import APIClient
from rest_framework import status
from tags.models import Tag
from users.models import CustomUser
from tags.serializers import TagAdminSerializer

@pytest.mark.django_db
class TestTagSerializers:

    def test_tag_admin_serializer(self):
        user = CustomUser.objects.create_user(username='admin', password='admin123')
        tag = Tag.objects.create(
            owner=user,
            pet_name="Buddy",
            gender="Male",
            disease="None",
            recommended_medicine="None",
            subscription_choice="Monthly",
            subscription_id="123abc",
            delivery_address="123 Pet Street",
            qr_code="dummy_qr_code"
        )
        serializer = TagAdminSerializer(tag)
        assert serializer.data['qr_code'] == "dummy_qr_code"

# tags/tests/test_serializers.py

@pytest.mark.django_db
class TestTagSerializers:

    def test_tag_admin_serializer_invalid_data(self):
        invalid_data = {}  # Provide some invalid data here
        serializer = TagAdminSerializer(data=invalid_data)
        assert not serializer.is_valid()



@pytest.mark.django_db
class TestTagSerializers:

    def test_tag_admin_serializer_no_qr_code(self):
        user = CustomUser.objects.create_user(username='admin', password='admin123')
        tag = Tag.objects.create(
            owner=user,
            pet_name="Buddy",
            gender="Male",
            disease="None",
            recommended_medicine="None",
            subscription_choice="Monthly",
            subscription_id="123abc",
            delivery_address="123 Pet Street",
        )
        serializer = TagAdminSerializer(tag)
        assert 'qr_code' in serializer.data



@pytest.mark.django_db
class TestTagSerializers:

    def test_tag_serializer_invalid_subscription_id(self):
        user = CustomUser.objects.create_user(username='admin', password='admin123')
        initial_tag = Tag.objects.create(
            owner=user,
            pet_name="Initial",
            gender="Male",
            disease="None",
            recommended_medicine="None",
            subscription_choice="Monthly",
            subscription_id="123abc",
            delivery_address="123 Pet Street",
        )
        duplicate_tag_data = {
            "pet_name": "Duplicate",
            "gender": "Female",
            "disease": "None",
            "recommended_medicine": "None",
            "subscription_choice": "Monthly",
            "subscription_id": "123abc",  # Same as initial_tag
            "delivery_address": "456 New Street",
        }
        serializer = TagAdminSerializer(data=duplicate_tag_data)
        assert not serializer.is_valid()
        assert 'subscription_id' in serializer.errors
