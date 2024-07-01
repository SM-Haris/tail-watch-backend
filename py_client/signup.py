import requests

# SignUp endpoint
signup_endpoint = "http://localhost:8000/api/auth/signup/"
signup_data = {
    'username': "test_user_4",
    'password': '12345678',
    'email':'test@gmail.com',
    'address':'test_address',
    'phone_number':'12345678'
}

# Authenticate and get the token
signup_response = requests.post(signup_endpoint, json=signup_data)
print(signup_response.json())

