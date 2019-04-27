import requests

res = requests.get('http://192.168.99.100:5000/')

str = (res.text)
str2 = str.replace('World!', '!')

# If-statement after search() tests if it succeeded
print (str2)
