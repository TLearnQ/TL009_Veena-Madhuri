
import requests

api_url = "https://httpbin.org/get"
headers = {
    "Authorization": "Bearer mytoken"
}

response = requests.get(api_url, headers=headers)
data = response.json()
auth_header = data["headers"]["Authorization"]

token = auth_header.split("Bearer ")[1]
token_length = len(token)

print(token_length)