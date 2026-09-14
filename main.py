import requests

response = requests.get("https://randomuser.me/api/", json=False)
cara = response.json()
nome_usuario = cara.get('name')

print(nome_usuario)
