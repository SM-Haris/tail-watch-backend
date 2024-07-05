import pytest
from tags.models import Tag
from tags.serializers import TagSerializer
from users.models import CustomUser

@pytest.mark.django_db
class TestTagSerializers:

    def test_tag_admin_serializer(self):
        user = CustomUser.objects.create_user(username='admin', password='admin123',email='test@gmail.com', address='test-address', phone_number='12345678',)
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
        serializer = TagSerializer(tag)
        assert serializer.data['qr_code'] == "dummy_qr_code"

# tags/tests/test_serializers.py

@pytest.mark.django_db
class TestTagSerializers:

    def test_tag_admin_serializer_invalid_data(self):
        invalid_data = {}  # Provide some invalid data here
        serializer = TagSerializer(data=invalid_data)
        assert not serializer.is_valid()



@pytest.mark.django_db
class TestTagSerializers:

    def test_tag_admin_serializer_no_qr_code(self):
        user = CustomUser.objects.create_user(username='admin', password='admin123',email='test@gmail.com', address='test-address', phone_number='12345678',)
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
        serializer = TagSerializer(tag)
        assert 'qr_code' in serializer.data



@pytest.mark.django_db
class TestTagSerializers:

    def test_tag_serializer_invalid_subscription_id(self):
        user = CustomUser.objects.create_user(username='admin', password='admin123',email='test@gmail.com', address='test-address', phone_number='12345678',)
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
        serializer = TagSerializer(data=duplicate_tag_data)
        assert not serializer.is_valid()
        assert 'subscription_id' in serializer.errors
