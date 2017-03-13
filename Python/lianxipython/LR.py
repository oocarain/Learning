#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

#核酸TM值计算
import primer3
import re
with open('ceshi.txt','r') as f:
    my_ncfile = f.read()
    a = re.findall(r'(?m)(^>[\w]+)\n([\w\n]+)',my_ncfile)
    for i in range(len(a)):
        deal_n = a[i][1]
        deal_n_over = re.sub(r'\n','',deal_n)
        tm = tmfun(deal_n_over)#这里面那个函数名我忘记了
        print a[i][0]
        print tm
        #print('%s==>%s'%(a[i][0],tm))#这个是Python输出格式







