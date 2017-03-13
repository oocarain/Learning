#!/usr/bin/python
# -*- coding: UTF-8 -*-
#分子分母化简问题

def simplify():
    aword = input('please input numerator and denominator(exp format:ab bcd):') 
    length = len(aword)
    for k in range(length-1):
        while aword[k] ==' ':
            space_index = k
            break
#将用户输入拆分为分子a和分母b
    a = aword[:space_index]
    b= aword[space_index+1:]
#找出a,b中相同字母
    a_list =list(a)
    b_list =list(b)
    pop_a =[]
    for i in range(len(a_list)):
        for j in range(len(b_list)):
            if a_list[i]==b_list[j]:
                pop_a.append( a_list[:].pop(i))
                
#去除a,b相同字母，将剩下的重新链接为字符串                
    for m in range(len(pop_a)):
        a_list.remove(pop_a[m])
        b_list.remove(pop_a[m])

    c =''.join(a_list)
    d=''.join(b_list)
#根据不同情况输出最终化简结果
    if c=='' and d=='':
        print(a,'/',b,'=','1')
    elif c=='' and d!='':
        print(a,'/',b,'=','1/',d)
    elif c!='' and d=='':
        print(a,'/',b,'=',c)
    else:
        print(a,'/',b,'=',c,'/',d)
    
