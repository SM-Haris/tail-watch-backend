from django.conf import settings
from django.db import models

from users.models import CustomUser

class Tag(models.Model):
    owner = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    disease = models.CharField(max_length=100)
    recommended_medicine = models.CharField(max_length=200)
    qr_code = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
