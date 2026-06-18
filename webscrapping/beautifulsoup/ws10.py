from bs4 import BeautifulSoup
import requests

url = "https://www.brilliantcomputers.in"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

allpara = soup.find_all("p")

# Open file with UTF-8 encoding
with open("contents.txt", "w", encoding="utf-8") as f:
    for i in allpara:
        f.write(i.get_text(strip=True) + "\n")