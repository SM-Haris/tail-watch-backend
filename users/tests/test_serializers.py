import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from users.serializers import CustomUserCreationSerializer, CustomUserUpdateSerializer

@pytest.mark.django_db
class TestCustomUserSerializers:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        self.valid_user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "Mm34567*",
            "address": "123 Test St",
            "phone_number": "1234567890",
        }
        self.invalid_user_data = {
            "username": "testuser",
            "email": "invalidemail",  # Invalid email format
            "password": "Mm34567*",
            "address": "123 Test St",
            "phone_number": "1234567890",
        }

    def test_custom_user_creation_serializer_valid_data(self):
        serializer = CustomUserCreationSerializer(data=self.valid_user_data)
        assert serializer.is_valid()

    def test_custom_user_creation_serializer_invalid_data(self):
        serializer = CustomUserCreationSerializer(data=self.invalid_user_data)
        assert not serializer.is_valid()
        assert 'email' in serializer.errors

    def test_custom_user_update_serializer(self):
        User = get_user_model()
        user = User.objects.create_user(**self.valid_user_data)
        updated_data = {
            "phone_number": "9876543210",
            "address": "456 Updated St",
        }
        serializer = CustomUserUpdateSerializer(user, data=updated_data, partial=True)
        assert serializer.is_valid()
        updated_user = serializer.save()
        assert updated_user.phone_number == updated_data['phone_number']
