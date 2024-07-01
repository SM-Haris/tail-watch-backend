import uuid
from django.db import models

from .utils import GenerateQrCodeImage
from users.models import CustomUser
from django.utils.translation import gettext_lazy as _

from users.models import CustomUser

class Tag(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = 'Male', _('Male')
        FEMALE = 'Female', _('Female')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices, default=GenderChoices.MALE)
    disease = models.CharField(max_length=100, null=True)
    recommended_medicine = models.CharField(max_length=200, null=True)
    qr_code = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.qr_code = GenerateQrCodeImage(self.id)
        super().save(*args, **kwargs)
