import requests
params = {
    "q": "python"
}

response = requests.get(
    "https://www.google.com/search/",
    params=params
)

print(response.url)
