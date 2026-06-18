from bs4 import BeautifulSoup
import requests
url="https://www.w3schools.com/html/html_tables.asp"
response=requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
rows = soup.find_all("tr")
for row in rows:

    cols = row.find_all(
        ["td", "th"]
    )

    data = [
        col.text.strip()
        for col in cols
    ]

    print(data)
