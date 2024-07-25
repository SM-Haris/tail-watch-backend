import pytest
from rest_framework.test import APIClient,APITestCase
from django.urls import reverse
from tags.models import Tag
from history.models import History
from users.models import CustomUser


@pytest.mark.django_db
class TestHistoryViews(APITestCase):
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


    def test_history_create_view(self):
        data = {
            "tag": self.tag.id,
            "longitude": "12.3456789",
            "latitude": "98.7654321",
        }
        url = reverse("history-create")
        response = self.client.post(url, data, format="json")
        assert response.status_code == 201

    def test_history_list_view(self):
        History.objects.create(
            tag=self.tag,
            longitude=12.3456789,
            latitude=98.7654321,
        )
        self.client.force_authenticate(user=self.user)
        url = reverse("history-list", args=[str(self.tag.id)])
        response = self.client.get(url)
        print(response)
        assert response.status_code == 200