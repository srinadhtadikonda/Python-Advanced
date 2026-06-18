#program to fetch a paragraph

from bs4 import BeautifulSoup
import requests
url="https://www.brilliantcomputers.in"
response=requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
para=soup.find("p")
print(para)