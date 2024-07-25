import requests

# Login endpoint
login_endpoint = "http://localhost:8000/api/auth/login/"
login_data = {"username": "test_user_1", "password": "Mm34567*("}

# Authenticate and get the token
auth_response = requests.post(login_endpoint, json=login_data)
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()["access"]
    headers = {"Authorization": f"Bearer {token}"}

    history_creation_endpoint = "http://localhost:8000/api/history/"
    history_list_endpoint = "http://localhost:8000/api/history/d1846c2b-6aaa-4970-ad94-50c9a97a24cd/"


    data = {
        "latitude": 31.599258,
        "longitude": 74.340672,
        "tag":"d1846c2b-6aaa-4970-ad94-50c9a97a24cd"
    }

    # To create history
    create_history_response = requests.post(history_creation_endpoint, json=data)
    print(create_history_response.json())

    # # To fetch history
    # list_history_response = requests.get(history_list_endpoint,headers=headers)
    # print(list_history_response.json())


else:
    print("Authentication failed")
