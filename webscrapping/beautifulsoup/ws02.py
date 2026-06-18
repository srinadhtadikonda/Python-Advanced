import requests 
url="https://www.brilliantcomputers.in"
response=requests.get(url)
print(response.text[:500])