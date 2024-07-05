# tags/tests/test_views.py

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from tags.models import Tag
from users.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken

class TagAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', password='12345'
        )
        self.tag = Tag.objects.create(
            owner=self.user,
            pet_name='Buddy',
            gender='Male',
            disease='None',
            recommended_medicine='None',
            subscription_id='sub_12345',
            delivery_address='123 Street',
            subscription_choice='Monthly'
        )
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_tag_list(self):
        url = reverse('tag-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tag_create(self):
        url = reverse('tag-list-create')
        data = {
            'pet_name': 'Buddy2',
            'gender': 'Male',
            'disease': 'None',
            'recommended_medicine': 'None',
            'subscription_id': 'sub_123456',
            'delivery_address': '456 Street',
            'subscription_choice': 'Monthly'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_tag_detail(self):
        url = reverse('tag-detail', args=[str(self.tag.id)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tag_update(self):
        url = reverse('tag-update', args=[str(self.tag.id)])
        data = {'pet_name': 'Buddy Updated'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.pet_name, 'Buddy Updated')

    def test_tag_delete(self):
        url = reverse('tag-delete', args=[str(self.tag.id)])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
