import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Main_Page'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.select('h1')

for title in titles:
    print(title.get_text())


with open('titles.txt', 'w') as f:
    for title in titles:
        f.write(title.get_text()+"\n")