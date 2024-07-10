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
    auth_users_endpoint = "http://localhost:8000/api/auth/me/"
    user_update_endpoint = "http://localhost:8000/api/auth/update/"

    data = {
        "pet_name": "pet_5",
        "gender": "Male",
        "disease": "random",
        "recommended_medicine": "random",
        "subscription_choice": "Monthly",
        "subscription_id": "888889423",
        "delivery_address": "random",
    }

    user_update_data = {
        "email" : "testing@gmail.com",
        "password": "Mm34567*"
    }

    bulk_data = [
        {
            "pet_name": "pet_13",
            "gender": "Male",
            "disease": "random",
            "recommended_medicine": "random",
            "subscription_choice": "Monthly",
            "subscription_id": "1234534534",
            "delivery_address": "random",
        },
        {
            "pet_name": "pet_14",
            "gender": "Female",
            "disease": "random",
            "recommended_medicine": "random",
            "subscription_choice": "Monthly",
            "subscription_id": "43124534534",
            "delivery_address": "random",
        },
    ]

    # # To create tags
    # create_tags_response = requests.post(tags_endpoint, headers=headers, json=data)
    # print(create_tags_response.json())

    # # To create bulk tags
    # bulk_tags_response = requests.post(tags_bulk_endpoint, headers=headers, json=bulk_data)
    # print(bulk_tags_response.json())

    # # To fetch user tags
    # my_tags_response = requests.get(tags_endpoint, headers=headers)
    # print(my_tags_response.json())

    # # To fetch users details
    # user_detail_response = requests.get(auth_users_endpoint, headers=headers)
    # print(user_detail_response.json())

    # # To update user data
    # update_response = requests.patch(user_update_endpoint, headers=headers, json=user_update_data)
    # print(update_response.json())

else:
    print("Authentication failed")
