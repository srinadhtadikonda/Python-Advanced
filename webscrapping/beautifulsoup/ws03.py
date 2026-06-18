import requests

headers = {
    "User-Agent":
    "Mozilla/5.0"
}

response = requests.get(
    "https://brilliantcomputers.in",
    headers=headers
)

print(response.status_code)
