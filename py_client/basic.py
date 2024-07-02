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

    data = {
        "pet_name": "pet_3",
        "gender": "Male",
        "disease": "random",
        "recommended_medicine": "random",
        "qr_code": "iVBORw0KGgoAAAANSUhEUgAAAZoAAAGaAQAAAAAefbjOAAADKElEQVR4nO2bQY6rOBCGvxos9ZJIfYAcxdzgHWk0R+ob4KPkAE/Cy0hG/yywIWnN5qkz0J0UC4SMP1EWpXL5L9vEH1/prz9nwCGHHHLIIYccek7I6hWWJ5KF5bUNOWBDbh2GQ8xzaEcISRJRkjR1klQAOkkT61Onm37jNx+TQ4+AcgsA6QQatw79dXlh1uLGjxmTQw+B4iUAfYF0lm5949FfcuhbQuG/Gi1eQoFsQN8J8gO+5NDPgJpH9GL58elXCUrnAvQTFj8MAdwqWd98TA59BaoekQyADouXN1m8hFIDBV2x+DHbMeY5tDu0eMRNAEjnAul8NeivJvJsNYIcYZ5DB0Fmp9lsyKEuM+IE+sfeBHSCvMoTh5jn0O56hDR1gv5OlIjtprFvT3I94tmhqlDRFxZnGHup+UF7MVL9xRWq54eaZjl1akFhCxmFFi20zB8eI54fajGCbk0e66yxqNhxam116nCPeBVotvrPp6ZYp1O3aJaSrsbiFkeZ59BeUF1ExBEgB5TOBaUBLGo2QVfsNoLsa55Du0Nt+UBNHGoC2dKKOnWo5p0+azw/tMSIqkjmgMgG6dQB+V0WxxJEPmH01yZcfvMxOfQAKKrQKp4FaZoXzRLoRDqx5piHmOfQ/pWu/F6UhoDFCRl9CSQDkU9r3062t3kO7Q6teQSLNFlv1JyBuG6fAnz1+QLQ3f6IHCBOM9D/thYjgPTrd/Bq+ItALbPsJ4iaA3VyCAjmUAugS5fVLb75mBz6CrTuvK0rzUWuHLcyB9QXI/is8QLQfV2jpQv0WuVKraK21zVeAbqtfY6bNNlvdY37NveIZ4fWKKB1SdHdhYcteLhHvBC0nenS2F/Nhr5QT3KdZmt7qNZo8SPG5NAXNUtpK3/X41xtS1UteOSADceY59D+UDvTZUN+axsrl7bZSGZW3eIg8xzaDVrXGrQscvvxW3rZyqOeR7wepDGHKkroEupmfQD7WwUbDjbPof8d+nymy+pJrndZ/OiKxWlGyVhuu5vn0O7Qus8SqKuJ7mbb5aZW1OTTZ41nhz6f6dL9bW3zXXUOOeSQQw455NDn61/d3WHYH8ScPwAAAABJRU5ErkJggg==",
        "subscription_choice": "Monthly",
        "subscription_id": "8888",
        "delivery_address": "random",
        "created_at": "2024-07-02T13:33:29.556352Z",
    }

    # To create tags
    get_response = requests.post(tags_endpoint, headers=headers, json=data)

    # To fetch user tags
    # get_response = requests.get(tags_endpoint, headers=headers)

    print(get_response.json())
else:
    print("Authentication failed")
