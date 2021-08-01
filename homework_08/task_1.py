import requests


ggg = requests.get('https://api.exchangerate.host/convert').json()
print(ggg['date'])