import requests

res = requests.get('http://192.168.99.100:5000/')
res.raise_for_status()

print(res.text)
