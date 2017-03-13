#!/usr/bin/env python
#-*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup


def getHTHLtext(url):
    try:
        htmltext = requests.get(url,timeout=30)
        htmltext.raise_for_status()
        htmltext.encoding = htmltext.apparent_encoding
        return htmltext.text
    except:
        print('scraping error')
url = "http://www.pythonscraping.com/pages/warandpeace.html"
html = getHTHLtext(url)
soup = BeautifulSoup(html,'html.parser')
nameList = soup.find_all('span',{'class':'green'})
for name in nameList:
    print(name.string)
