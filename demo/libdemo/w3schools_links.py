import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.w3schools.com")
tree = BeautifulSoup(resp.text, 'html.parser')

for a in tree.find_all('a'):
    if 'href' not in a.attrs:
        continue

    href = a['href']
    if href != "#":
        if href.startswith("http"):
            print(href)
        else:
            print("https://www.w3schools.com/" + href)
