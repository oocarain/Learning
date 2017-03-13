#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

#---------------------------------------
import requests
def get_ama(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[1500:2000])
    except:
        print('爬取失败')

url = 'https://www.amazon.cn/dp/B00DMS9990/ref=cngwdyfloorv2_recs_0?pf_rd_p=7645736c-6759-4677-9dfb-2a3fd04770aa&pf_rd_s=desktop-2&pf_rd_t=36701&pf_rd_i=desktop&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=2V2W9A729786R1HP17VA&pf_rd_r=2V2W9A729786R1HP17VA&pf_rd_p=7645736c-6759-4677-9dfb-2a3fd04770aa'
get_ama(url)
#--------------------------------
import requests
def search_baidu(keywords):
    kv = {'wd':keywords}
    url = "http://www.baidu.com/s"
    try:
        r = requests.get(url,params = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('访问的连接为:',r.request.url)
        print('返回的搜索结果大小为:',len(r.text)/1024,'Kb')
    except:
        print('搜索失败')
search_baidu("Python")

#--------------------------------------
import requests
import os
store_site = "G://pics//"
url = "http://image.nationalgeographic.com.cn/2015/1030/20151030042921813.jpg"
path = store_site + url.split('/')[-1]
try:
    if not os.path.exists(store_site):
        os.mkdir(store_site)
    if not os.path.exists(path):
        r = requests.get(url)
        with open (path,'wb') as f:
            f.write(r.content)
            print('保存成功')
    else:
        print('文件已存在')
except:
    print('保存失败')
#-------------解析ip地址------------------
import requests
url = "http://m.ip138.com/ip.asp?ip="
try:
    r = requests.get(url+'202.204.80.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-1000:])
except:
    print('爬取失败')
http://python123.io/ws?k=v&x=y
