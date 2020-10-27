import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")
bs = BeautifulSoup(resp.text, "xml")
for item in bs.find_all("item")[:5]:
    print(item.find('title').text.strip())
    print(item.find('pubDate').text.strip())
    print('-' * 80)
