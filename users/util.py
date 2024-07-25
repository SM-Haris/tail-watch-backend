import os
from django.core.mail import send_mail
from rest_framework.exceptions import ValidationError

def send_password_reset_email(user, token):

    reset_link = f"http://tail_watch/password-reset-confirm/?uid={user.id}&token={token}"

    try:
      send_mail(
          from_email="smh261290@gmail.com",
          recipient_list=[user.email],
          subject="Pet Location Alert",
          message="",
          html_message=f"<p>Follow this link to reset your password {reset_link}<p>",
          fail_silently=False
      )
    except Exception as e:
        raise ValidationError("Invalid Email provided by user")

