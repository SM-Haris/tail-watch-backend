import uuid
from django.db import models

from .utils import GenerateQrCodeImage
from users.models import CustomUser
from django.utils.translation import gettext_lazy as _

from users.models import CustomUser
from .validators import validate_gender, validate_subscription_choice


class Tag(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = "Male", _("Male")
        FEMALE = "Female", _("Female")

    class SubscriptionChoices(models.TextChoices):
        MONTHLY = "Monthly", _("Monthly")
        YEARLY = "Yearly", _("Yearly")
        LIFETIME = "Lifetime", _("Lifetime")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=100, null=True)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
        default=GenderChoices.MALE,
        validators=[validate_gender],
    )
    disease = models.CharField(max_length=100, null=True)
    recommended_medicine = models.CharField(max_length=200, null=True)
    qr_code = models.TextField(blank=True)
    subscription_id = models.CharField(unique=True,max_length=200, null=False)
    delivery_address = models.CharField(max_length=200, null=False)
    subscription_choice = models.CharField(
        max_length=8,
        choices=SubscriptionChoices.choices,
        default=SubscriptionChoices.MONTHLY,
        validators=[validate_subscription_choice],
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.qr_code = GenerateQrCodeImage(self.id)
        super().save(*args, **kwargs)
