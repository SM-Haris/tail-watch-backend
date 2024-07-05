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
    tags_bulk_endpoint = "http://localhost:8000/api/tags/bulk/"
    auth_users_endpoint = "http://localhost:8000/api/auth/users/"
    auth_users_endpoint_query_search = "http://localhost:8000/api/auth/users/?search=test"
    user_update_endpoint = "http://localhost:8000/api/auth/update/"

    data = {
        "pet_name": "pet_3",
        "gender": "Male",
        "disease": "random",
        "recommended_medicine": "random",
        "subscription_choice": "Monthly",
        "subscription_id": "8888",
        "delivery_address": "random",
    }

    user_update_data = {
        "email" : "testing@gmail.com",
        "password": "Mm34567*"
    }

    bulk_data = [
        {
            "pet_name": "pet_10",
            "gender": "Male",
            "disease": "random",
            "recommended_medicine": "random",
            "subscription_choice": "Monthly",
            "subscription_id": "12344",
            "delivery_address": "random",
        },
        {
            "pet_name": "pet_11",
            "gender": "Female",
            "disease": "random",
            "recommended_medicine": "random",
            "subscription_choice": "Monthly",
            "subscription_id": "43124",
            "delivery_address": "random",
        },
    ]

    # To create tags
    # get_response = requests.post(tags_endpoint, headers=headers, json=data)

    # To create bulk tags
    # get_response = requests.post(tags_bulk_endpoint, headers=headers, json=bulk_data)

    # To fetch user tags
    # get_response = requests.get(tags_endpoint, headers=headers)

    # To fetch users data will return all users for admin
    # get_response = requests.get(auth_users_endpoint, headers=headers)

    # To fetch users data will return all users for admin
    # get_response = requests.get(auth_users_endpoint_query_search, headers=headers)

    # To update user data
    get_response = requests.patch(user_update_endpoint, headers=headers, json=user_update_data)

    print(get_response.json())
else:
    print("Authentication failed")
