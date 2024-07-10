import requests


def get_location_from_coordinates(latitude, longitude):
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}&zoom=18&addressdetails=1&accept-language=en"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        address = data.get("display_name", "Location not found")
        return address
    return "Location not found"
