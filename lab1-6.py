import re
import requests
import csv
import bs4
from bs4 import BeautifulSoup
url="https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
source_code=requests.get(url)
plain_text=source_code.text
soup = BeautifulSoup(plain_text,'html.parser')
#<a href="/wiki/Alabama" title="Alabama">Alabama</a>
#<td><a href="/wiki/Newark,_New_Jersey" title="Newark, New Jersey">Newark</a>
#txt=re.compile(r'<a.*?href="([^"]*)".*?>([\S\s]*?)</a>')
t =soup.find("table",class_="wikitable sortable plainrowheaders")# we need to look through the html code, and find out the tag,label,class of data
t3=t.find("tbody").findAll("a")
fp = open("pl5.txt", "w")
for content in t3:
    #print(content)
    contents=content.get('title')
    fp.write(str(contents)+'\r');
fp.close()