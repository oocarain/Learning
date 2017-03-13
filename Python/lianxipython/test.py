#!/usr/bin/env python
#-*- coding:UTF-8 -*-

#中国大学排名的定向爬虫
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLTEXT(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUniverList(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            for link in tds[1].find_all('a'):
                get_link = link.get('href')
            ulist.append([tds[0].string,tds[1].string,get_link])

def printUnivList(ulist,num):
    tpl = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tpl.format('排名','学校名称','链接',chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tpl.format(u[0],u[1],u[2],chr(12288)))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/ARWU2016.html'
    html = getHTMLTEXT(url)
    fillUniverList(uinfo,html)
    printUnivList(uinfo,20) #print tweteen university rank data
main()
