import requests

# Login endpoint
login_endpoint = "http://localhost:8000/api/auth/login/"
login_data = {"username": "test_user_1", "password": "Mm34567*"}

# Authenticate and get the token
auth_response = requests.post(login_endpoint, json=login_data)
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()["access"]
    headers = {"Authorization": f"Bearer {token}"}

    # Fetch tags with the token
    tags_endpoint = "http://localhost:8000/api/tags/"
    auth_users_endpoint = "http://localhost:8000/api/auth/users/"

    data = {
        "pet_name": "pet_3",
        "gender": "Male",
        "disease": "random",
        "recommended_medicine": "random",
        "subscription_choice": "Monthly",
        "subscription_id": "8888",
        "delivery_address": "random",
        "created_at": "2024-07-02T13:33:29.556352Z",
    }

    # To create tags
    get_response = requests.post(tags_endpoint, headers=headers, json=data)

    # To fetch user tags
    # get_response = requests.get(tags_endpoint, headers=headers)

    # To fetch users data will return all users for admin
    # get_response = requests.get(auth_users_endpoint, headers=headers)

    print(get_response.json())
else:
    print("Authentication failed")
