import uuid
from django.test import TestCase
from tags.models import Tag
from users.models import CustomUser

class TagModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', password='12345',email='test@gmail.com', address='test-address', phone_number='12345678',
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

    def test_tag_creation(self):
        self.assertEqual(self.tag.pet_name, 'Buddy')
        self.assertEqual(self.tag.owner.username, 'testuser')
        self.assertIsInstance(self.tag.id, uuid.UUID)

    def test_tag_qr_code_generation(self):
        self.assertTrue(self.tag.qr_code.startswith('iVBORw0KGgoAAAANSUhEUgAAA'))  # Base64 string check
