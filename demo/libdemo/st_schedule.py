import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com/default.aspx")
bs = BeautifulSoup(resp.text, "html.parser")

table = bs.find('table', id='ctl00_ContentPlaceHolder1_GridView2')
rows = table.find_all('tr')[1:]  # take all rows except first row
for row in rows:
    cols = row.find_all('td')
    print(f"{cols[0].text:35} {cols[4].text:10} {cols[1].text:15} {cols[2].text}")
