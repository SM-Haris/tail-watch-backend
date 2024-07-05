import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model


@pytest.mark.django_db
class TestLoginView:

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="Mm34567*",
        )

    def test_login_success(self):
        url = reverse('login')
        data = {"username": "testuser", "password": "Mm34567*"}
        response = self.client.post(url, data, format="json")
        print(response)
        assert response.status_code == status.HTTP_200_OK
        assert "access" in response.data
        assert "refresh" in response.data

    def test_login_failure(self):
        url = reverse('login')
        data = {"username": "testuser", "password": "Mm34589*"}
        response = self.client.post(url, data, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_login_failure_missing_field(self):
        url = reverse('login')
        data = {"username": "testuser"}
        response = self.client.post(url, data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestSignupView:

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.client = APIClient()

    def test_signup_success(self):
        url = reverse('signup')
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "Mm34567*",
            "address": "789 New St",
            "phone_number": "9876543210",
        }
        response = self.client.post(url, data, format="json")
        print(response)
        assert response.status_code == status.HTTP_201_CREATED

    def test_signup_failure_missing_field(self):
        url = reverse('signup')
        data = {
            "username": "newuser",
            "email": "testuser@example.com",
            "password": "Mm34567*",
            "phone_number": "1234567890",
        }
        response = self.client.post(url, data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_signup_failure_invalid_password(self):
        url = reverse('signup')
        data = {
            "username": "newuser",
            "email": "testuser@example.com",
            "password": "Mm345675",
            "address": "123 Test St",
            "phone_number": "1234567890",
        }
        response = self.client.post(url, data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestUserUpdateAPIView:

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="Mm34567*",
            address="123 Test St",
            phone_number="1234567890",
        )
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="adminpassword",
        )
        self.client.force_authenticate(user=self.user)

    def test_user_update_success(self):
        url = reverse('user-update')
        data = {
            "phone_number": "9998887777",
            "address": "Updated Address",
        }
        response = self.client.patch(url, data, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["phone_number"] == "9998887777"

    def test_user_update_failure(self):
        url = reverse('user-update')
        data = {
            "password": "invalidemail",  
        }
        response = self.client.patch(url, data, format="json")
        print(response)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_user_update_success_from_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        url = reverse('user-update')
        data = {
            "phone_number": "9998887777",
            "address": "Updated Address",
        }
        response = self.client.patch(url, data, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["phone_number"] == "9998887777"


# @pytest.mark.django_db
# class TestUserListAPIView:

#     @pytest.fixture(autouse=True)
#     def setUp(self):
#         self.client = APIClient()
#         self.user = get_user_model().objects.create_user(
#             username="testuser",
#             email="testuser@example.com",
#             password="Mm34567*",
#         )
#         self.admin_user = get_user_model().objects.create_superuser(
#             username="admin",
#             email="admin@example.com",
#             password="adminpassword",
#         )
#         self.client.force_authenticate(user=self.user)

#     def test_user_list_view(self):
#         url = reverse('user-list')
#         response = self.client.get(url)
#         assert response.status_code == status.HTTP_200_OK
#         assert len(response.results) == get_user_model().objects.count()

#     def test_user_list_search(self):
#         url = reverse('user-list') + '?search=testuser'
#         response = self.client.get(url)
#         assert response.status_code == status.HTTP_200_OK
#         assert len(response.data) == 1
#         assert response.data[0]["username"] == "testuser"
