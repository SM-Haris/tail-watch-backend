# users/tests/test_models.py

import pytest
from django.contrib.auth import get_user_model
from users.models import CustomUser

@pytest.mark.django_db
class TestCustomUserModel:

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
        )
        assert user.username == 'testuser'
        assert user.email == 'testuser@example.com'
        assert user.is_active
        assert not user.is_staff
        assert not user.is_superuser

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpassword',
        )
        assert admin_user.username == 'admin'
        assert admin_user.email == 'admin@example.com'
        assert admin_user.is_active
        assert admin_user.is_staff
        assert admin_user.is_superuser
