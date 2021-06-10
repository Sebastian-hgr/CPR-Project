import requests


myObject = {"number":"3"}

url = "http://localhost:3000/data"

x = requests.post(url, data = myObject)
print(x.text)