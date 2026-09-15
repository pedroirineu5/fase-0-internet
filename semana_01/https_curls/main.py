import requests

response = requests.get("https://randomuser.me/api/")
cara = response.json()
print(cara)
