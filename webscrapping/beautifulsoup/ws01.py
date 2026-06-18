import requests

response = requests.get("https://www.indi.com")
print(response.status_code)
print(response.text)
