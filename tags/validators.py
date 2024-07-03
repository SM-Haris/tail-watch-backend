from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_gender(value):
    valid_genders = ["Male", "Female"]
    if value not in valid_genders:
        raise ValidationError(
            _("%(value)s is not a valid gender"),
            params={"value": value},
        )


def validate_subscription_choice(value):
    valid_choices = ["Monthly", "Yearly", "Lifetime"]
    if value not in valid_choices:
        raise ValidationError(
            _("%(value)s is not a valid subscription choice"),
            params={"value": value},
        )
