from bs4 import BeautifulSoup
import requests
url="https://www.brilliantcomputers.in"
response=requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
heading=soup.find_all("h1")
print(heading)