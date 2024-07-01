import re
from django.core.exceptions import ValidationError

def validate_password(value):
    if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+}{":;\'?><,./\|~\-\\\[\]])[0-9a-zA-Z!@#$%^&*()_+}{":;\'?><,./\|~\-\\\[\]]{8,}$', value):
        raise ValidationError('Password must contain at least 8 characters, including uppercase, lowercase, digits, and special characters.')
