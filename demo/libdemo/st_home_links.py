import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com")
tree = BeautifulSoup(resp.text, 'html.parser')

for a in tree.find_all('a'):
    if 'href' not in a.attrs:
        continue

    href = a['href']
    if href != "#":
        if href.startswith("http"):
            print(href)
        else:
            print("http://www.srikanthtechnologies.com/" + href)
