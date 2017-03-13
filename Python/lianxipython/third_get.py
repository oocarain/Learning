#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import requests
urls_dict = {
    '电子工业出版社':'http://www.phei.com.cn/',
    '在线资源':'http://www.phei.com.cn/module/zygl/zxzyindex.jsp',
    'xyz':'www.phei.com.cn',
    'liunx运维':
    'http://www.phei.com.cn/module/goods/wssd_content.jsp?bookid=47235',
    'linux宝典':
    'http://www.phei.com.cn/module/goods/wssd_content.jsp?bookid=39745'
}
urls_lst = [

    ( '电子工业出版社','http://www.phei.com.cn/'),
    ('在线资源','http://www.phei.com.cn/module/zygl/zxzyindex.jsp'),
    ('xyz','www.phei.com.cn'),
    ('liunx运维','http://www.phei.com.cn/module/goods/wssd_content.jsp?bookid=47235'),
    ('linux宝典','http://www.phei.com.cn/module/goods/wssd_content.jsp?bookid=39745')
]

#利用字典抓去
crawled_urls_for_dict = set()
for ind,name in enumerate(urls_dict.keys()):
    name_url = urls_dict[name]
    if name_url in crawled_urls_for_dict:
        print(ind,name,'已经抓取过了')
    else:
        try:
            resp = requests.get(name_url)
        except Exception as e:
            print(ind,name,':',str(e)[0:50])
            continue
        content = resp.text
        crawled_urls_for_dict.add(name_url)
        with open ('bydict_'+name+'.html','w',encoding='utf8') as fget3:
            fget3.write(content)
            print('抓取完成:{}-->{},内容长度为:{}'.format(ind,name,len(content)))
for u in crawled_urls_for_dict:
    print(u)
print(' -'*20)

#利用列表抓取
crawled_urls_for_list = set()
for ind,tup in enumerate(urls_lst):
    name = tup[0]
    name_url = tup[1]
    if name_url in crawled_urls_for_list:
        print(ind,name,'已经抓取过了')
    else:
        try:
            resp = requests.get(name_url)
        except Exception as e:
            print(ind,'-->',name,':',str(e)[0:50])
            continue
    content = resp.text
    crawled_urls_for_list.add(name_url)
    with open('bylist_'+name+'.html','w',encoding='utf8') as fget4:
        fget4.write(content)
        print('抓取完成:{}-->{},内容长度为:{}'.format(ind,name,len(content)))
for v in crawled_urls_for_list:
    print(v)




