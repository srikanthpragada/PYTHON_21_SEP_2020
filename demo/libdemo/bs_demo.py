from bs4 import BeautifulSoup

text = """
<html>
 <body>
  <h1>Topics</h1>Here are topics
   <ul>
     <li>Requests</li>
     <li>Beautiful Soup</li>
     <li>DB API </li>
   </ul>
   <a href='http://www.srikanthtechnologies.com'>Website</a>
 </body>
</html>"""

tree = BeautifulSoup(text,'html.parser')

print(tree.h1.text)
for t in tree.find_all('li'):
    print(t.text)

print(tree.a['href'])