import requests

res = requests.get("https://twitter.com/explore")
print(res.text)

