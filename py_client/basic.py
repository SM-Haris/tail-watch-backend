import requests

# Login endpoint
login_endpoint = "http://localhost:8000/api/auth/login/"
login_data = {
    'username': "test_user_1",
    'password': '12345678'
}

# Authenticate and get the token
auth_response = requests.post(login_endpoint, json=login_data)
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['access']
    headers = {
        'Authorization': f"Bearer {token}"
    }
    
    # Fetch tags with the token
    tags_endpoint = "http://localhost:8000/api/tags/"

    data = {
        "pet_name":"test_pet_2",
        "gender": "male",
        "disease": "random",
        "recommended_medicine": "random",
        "qr_code": "random",
    }

    # To create tags
    get_response = requests.post(tags_endpoint, headers=headers,json=data)

    #To fetch user tags
    # get_response = requests.get(tags_endpoint, headers=headers)

    print(get_response.json())
else:
    print("Authentication failed")