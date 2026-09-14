import requests

response = requests.get("https://randomuser.me/api/")
cara = response.json()
nome_usuario = cara.get('name')

print(nome_usuario)
