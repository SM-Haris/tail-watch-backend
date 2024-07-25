import requests
from django.core.mail import send_mail
from rest_framework.exceptions import ValidationError

def get_location_from_coordinates(latitude, longitude):
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}&zoom=18&addressdetails=1&accept-language=en"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        address = data.get("display_name", "Location not verbally deduceable")
        send_email_notification(latitude, longitude, address)
        return address
    else:
        send_email_notification(latitude, longitude, "Location not verbally deduceable")
        return "Location not verbally deduceable"


def send_email_notification(latitude, longitude, location):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>Pet Location Alert</title>
      <style>
        body {{
          background-color: black;
          color: white;
          font-family: Arial, sans-serif;
        }}
        .location-box {{
          background-color: blue;
          color: white;
          padding: 10px;
          border-radius: 5px;
          text-align: center;
        }}
        .location-box p {{
          font-weight: bold;
        }}
      </style>
    </head>
    <body>

    <h1>Pet Location Alert</h1>

    <p>Your pet has been located!</p>

    <div class="location-box">
      <p>Longitude: {longitude}</p>
      <p>Latitude: {latitude}</p>
      <p>Address: {location}</p>
    </div>

    <p>Please use this information to locate your pet.</p>

    </body>
    </html>
    """

    try:
      send_mail(
          from_email="smh261290@gmail.com",
          recipient_list=["dev.muhammad.haris@gmail.com"],
          subject="Pet Location Alert",
          message="",
          html_message=html_content,
          fail_silently=False
      )
    except Exception as e:
        raise ValidationError("Invalid Email provided by user")
