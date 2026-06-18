from bs4 import BeautifulSoup
import requests

url = "https://www.brilliantcomputers.in"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

links = [a['href'] for a in soup.find_all('a', href=True)]

# Print each link on a new line
for link in links:
    print(link)