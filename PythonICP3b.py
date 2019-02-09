import requests
from bs4 import BeautifulSoup
url="https://en.wikipedia.org/wiki/Deep_learning"
source_code=requests.get(url)
print(source_code)
plain_text=source_code.text
soup = BeautifulSoup(plain_text,'html.parser')
print(soup.title)
t1 =soup.find_all('a')   #<a herf> on be behalf of the link to the other pages , but <a> can reprensent any URL like images
for t2 in t1:            #so the first step is to select 'a' and then use the result to select href
    t3 = t2.get('href')
    print(t3)
