#program to print the title
from bs4 import BeautifulSoup
import requests
url="https://www.brilliantcomputers.in"
response=requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links=[a['href'] for a in soup.find_all('a', href=True)]
print(links[:5])

#