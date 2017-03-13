#!usr/bin/python
#-*- encoding: UTF-8 -*-
sum = 0
for x in list(range(101)):
    if x%2==0:
         print(x,';',end=' ')
        if x%8==0:
        print('\n')
print('END')
#-----------------------------
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
#----------------------------
    #remove question
import math
def move(x,y,step,angle=0):
    nx=x + step*math.cos(angle)
    ny=y + step*math.sin(angle)
    return nx, ny
#----------------------------
#quadratic 计算一元二次方程的解
import math
def quadratic(a,b,c):
    if b**2-4*a*c >=0:
        result1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        result2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        return result1,result2
    else:
        print('方程无实数解')
#-----------------------------
#BMI 指标衡量体重状态
w = float (input ('请输入你的体重（单位：kg）:'))
h = float (input ('请输入你的身高（单位：M）:') )
bmi = w/h**2  #BMI指数衡量是否体重是否正常
if bmi <=18.5 :
    print ('过轻')
elif  bmi <= 25:
    print('正常')
elif bmi  <= 28:
    print('过重')
elif bmi <=32:
    print('肥胖')
else:
    print('严重肥胖')
#------------------------------
#递归计算n阶乘：
def fact(n):
        return fact_hah(n,1)


def fact_hah(num,product):
    if num==1:
        return product
    return fact_hah(num-1,num*product)

print('9!=',fact(9))
print('7!=',fact(7))
print('5!=',fact(5))

#------------------------------
#递归解决汉诺塔的问题
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
        return
    move(n-1, a, c, b)
    print('move', a, '-->', c)
    move(n-1, b, a, c)


print(move(3, 'A', 'B', 'C'))
print('-----------------------分割线----------------')
print(move(4, 'A', 'B', 'C'))
print('-----------------------分割线----------------')
print(move(5, 'A', 'B', 'C'))
#--------------------------------------
#从dict中提取key与value
mydict = {'a':1,'b':2,'c':3}
for key in mydict:
  print (key)

for value in mydict.values():
  print(value)

for k,v in mydict.items():
  print(k,'==>',v)
#-------------------------------
#对list实现下标循环--enumerate

mylist = list('Ilovechuntian')
for i,value in enumerate(mylist):
  print(i,' ',value)
#-------------------------------
#定义一个函数可以列出目录下所有的文件和文件夹

def findfile(path):
  count = 0
  import os
  whatinfile = [d for d in os.listdir(path)]
  for i in whatinfile:
    print (i,'  ',end='')
    count += 1
    if count % 3 == 0:
      print ('\n')

myfile = str(input('Please give me the path of your file:'))

print (findfile(myfile))

#-------------------------------
#isinstance 的一个例子
L1 = ['Hello','World',10,'AppLe',None]
L2 = [i.lower() for i in L1 if isinstance(i,str)]
print(L2)
#-------------------------------
#杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
#输出十行杨辉三角
t = triangles()
n =0
for i in t:
  print(i)
  n += 1
  if n ==10 :
    break
#-----------------------

def reverse_str(string):
    return string[::-1]

if __name__ =='__main__':
    mystring = 'hello cheng jia wen'
    print (reverse_str(mystring))
#-----------------------------------
#一个素数问题
#从三开始的奇数序列生成器

def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n

#定义一个筛选函数这个筛选函数

def _not_divisible(n):
    return lambda x : x % n > 0

#定义一个素数生产器

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

#输出小于1000的所有素数
count = 1
for n in primes():
    count = count + 1
    if n < 1000 :
        print (n,'  ',end = '')
        if count % 6 == 0:
            print('\n')
    else:
        break

#------------------------------
#回数
def is_palindrome(n):
    num2char = str(n)
    reverse_num2char = num2char[::-1]
    return num2char == reverse_num2char

out = filter(is_palindrome,range(1,1000))

count = 0
for i in out:
    count = count + 1
    print(i,'  ',end='')
    if count % 5 == 0:
        print('\n')

#------------------------------
#sorted
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(i):
    name = i[0]
    return name

def by_grade(j):
    grade = j[1]
    return grade

L2 = sorted(L,key = by_name)
print(L2)

L3 = sorted(L,key  = by_grade)
print(L3)
#------------------------------------------
#类的学习 :-)
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name
    def get_score(self):
        return  self.__score
    def set_score(self,score):
        if 0<= score <= 100:
             self.__score = score
        else:
            raise ValueError('bad score')
    def print_all(self):
        print('%s %s' % (self.__name,self.__score))
    def get_grade(self):
        if self.__score > 90:
            return 'A'
        elif self.__score > 60:
            return 'B'
        else:
            return 'C'
one_std = Student('Chengjiawen',56)
one_std.print_all()
print(one_std.get_name())
one_std.set_score(98)

one_std.print_all()

print(one_std.get_grade())

#-------------------------------------------
#定义一个父类
class Animal(object):
    def run(self):
        print('Animal is Running')

animal = Animal()
animal.run()
print('-'*20)
#下面是父类Animal的子类
class Dog(Animal):
    def run(self):
        print('Dog is Running')
    def eat(self):
        print('Dog is eating')
class Cat(Animal):
    def run(self):
        print('Cat is Running')
    def eat(self):
        print('Cat is eating')


dog = Dog()
dog.run()
dog.eat()
print(isinstance(dog,Animal))
print(isinstance(dog,Dog))

cat = Cat()
cat.run()
cat.eat()
print('-'*20)
def run_twice_animal(animal):
    animal.run()
    animal.run()

run_twice_animal(Animal())
print('\n')
run_twice_animal(Dog())
print('\n')
run_twice_animal(Cat())
print('-'*20)

class oocarain(Animal):
    def run(self):
        print('oocarain is not animal')

run_twice_animal(oocarain())
print('-'*20)
#-------------------------------------
#2017/2/4 22:32
class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,width):
        if not isinstance(width,int):
            raise ValueError('width must be integer')
        if width <0 or width >2000:
            raise ValueError('width must between 0 ~ 100')
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,height):
        if not isinstance(height,int):
            raise ValueError('height must be integer')
        if height <0 or height >2000 :
            raise ValueError('height must between 0 ~ 2000')
        self._height = height
    @property
    def resolution(self):
        return self._height * self._width

myscreen = Screen()
myscreen.width = 200
myscreen.height = 100

print (myscreen.width,myscreen.height,myscreen.resolution)

#---------------------------------------------
#验证码
from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('C:/windows/Fonts/Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')

#-------------------------------
def reverse_complement(seq):
    ntComplement = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}

    revSeqList = list(reversed(seq))
    revComSeqList = [ntComplement[k] for k in revSeqList]

    revComSeq = ''.join(revComSeqList)
    return revComSeq

seq = ''
with open('shan.txt') as f:
    for line in f:
        line = line.strip()
        seq += line.upper()

print (reverse_complement(seq))

#--------------------------------
from datetime import datetime
import os

pwd = os.path.abspath('.')
print(pwd)
print('      Size     Last Modified  Name')
print('-'*35)

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

#------------------------------
#批量修改文件名
import os
def rename():
    count = 0
    path=r'C:\Users\Administrator\Desktop\blogpic'
    filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
    for files in filelist:#遍历所有文件
        Olddir=os.path.join(path,files)#原来的文件路径
        if os.path.isdir(Olddir):#如果是文件夹则跳过
            continue
        filename=os.path.splitext(files)[0]#文件名
        filetype=os.path.splitext(files)[1]#文件扩展名
        Newdir=os.path.join(path,'bg-'+str(count)+filetype);#新的文件路径
        os.rename(Olddir,Newdir)#重命名
        count+=1
rename()

#-----------------------------------------

#用于正则表达式练习的数据生成器
from random import randrange,choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime
tlds = ('com','edu','net','org','gov')
for x in range(randrange(5,12)):
    date_int = randrange(maxsize)
    date_str = ctime(date_int)
    login_name_len = randrange(4,8)
    login_name = ''.join(choice(lc) for j in range(login_name_len))
    domain_len = randrange(login_name_len,13)
    domain = ''.join(choice(lc) for j in range(domain_len))
    with open('test_string.txt','a') as f:
        f.write('%s::%s@%s.%s::%d-%d-%d'%(date_str,login_name,domain,choice(tlds),
        date_int,login_name_len,domain_len)+'\n')

#-------------------
#提取上面生成文件中的日期
import re
with open('test_string.txt','r') as f:
    for eachline in f:
        print(re.findall(r'^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)',eachline))
print('-'*20)
#----------------------
import base64

s = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.b64decode(s).decode('utf-8')
print(d)

s = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d)
#----------------------
#bmp文件识别与获取相关参数
import struct
def ReadBMP(file):
    with open(file, 'rb') as f:
        bit_all=f.read()
        bit=bit_all[:30]
    return bit
def JudgeBMP(s):
    s1=struct.unpack('<ccIIIIIIHH', s)
    print('图像详细信息:',s1)
    if s1[0]==b'B' and s1[1]==b'M':
        print('windows位图')
        print('像素:',s1[6],'*',s1[7],'  颜色数:',s1[-1])
    elif s1[0]==b'B' and s1[1]==b'A':
        print('Os/2位图')
        print('像素:',s1[6],'*',s1[7],'  颜色数:',s1[-1])
    else:
        print('不是标准的位图文件')

if __name__=='__main__':
    f_name = input('请输入当前目录下位图名(e.g.:***.bmp):')
    binary_txt=ReadBMP(f_name)
    JudgeBMP(binary_txt)
#--------------------------------
#hashlib MD5摘要算法，写个小小的注册，登录
import hashlib
db = {}
def get_md5(mix_password):
    md5 = hashlib.md5()
    md5.update(mix_password.encode('utf-8'))
    return md5.hexdigest()

def register():
    username = input('Please input your username:')
    password = input('Please input your password:')
    if 5<len(username)<17 and 6<len(password)<17:
        db[username] = get_md5(password+username+'the-salt')
        print('Register success!please login')
        login()
    else:
        print('username and password must be 6-16 characters,try again')
        register()

def login():
    usn = input('Please enter your username:')
    pwd = input('Please enter your password:')
    if usn in db:
        md5 = hashlib.md5()
        md5.update((pwd+usn+'the-salt').encode('utf-8'))
        pwding =md5.hexdigest()
        if pwding == db[usn]:
            print('longin success')
        else:
            print('Password is not match,Please try again!')
    else:
        print('Username is not exist,please register first!')
        register()
login()

#-------------------------------
#hashlib MD5摘要算法，写个小小的注册，登录
#实现注册内容保存在本地的txt文本下
import hashlib
import re
import json

def get_md5(mix_password):
    md5 = hashlib.md5()
    md5.update(mix_password.encode('utf-8'))
    return md5.hexdigest()

def register():
    print('-'*15,'Register','-'*20)
    username = input('Please input your username:')
    password = input('Please input your password:')
    if 5<len(username)<17 and 5<len(password)<17:
        with open('register.txt','r') as fr:
            db = fr.read()
            passwordNB = get_md5(password+username+'the-salt')
            db_no_k = re.sub('[\}]','',db)
        with open('register.txt','w') as fw:
            add_db = db_no_k+','+'"'+username+'"'+':'+'"'+passwordNB+'"'+'}'
            fw.write(add_db)
            print('Register success!please login')
        login()
    else:
        print('username and password must be 6-16 characters,try again')
        register()

def login():
    print('-'*15,'login','-'*20)
    with open('register.txt','r') as f:
        database = f.read()
        database = re.sub('[\s]','',database)
        dict_database = json.loads(database)
    usn = input('Please enter your username:')
    pwd = input('Please enter your password:')
    if usn in dict_database:
        md5 = hashlib.md5()
        md5.update((pwd+usn+'the-salt').encode('utf-8'))
        pwding =md5.hexdigest()
        if pwding == dict_database[usn]:
            print('longin success')
        else:
            print('Password is not match,Please try again!')
    else:
        print('Username is not exist,please register first!')
        register()
login()

#------------------------
#上下文管理器
class oocarain(object):
    def pn(self):
        for i in range(10):
            print('hello:',i)
    def __enter__(self):
        print('--'*9,'BEGAIN','--'*9)
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type:
            print('ERROR')
        else:
            print('--'*10,'END','--'*10)
with oocarain() as e:
    e.pn()

#------------------
#核酸TM值计算
#import primer3
import re
with open('ceshi.txt','r') as f:
    my_ncfile = f.read()
    a = re.findall(r'(?m)(^>.+)\n(.+)',my_ncfile)
    for i in range(len(a)):
        deal_n = a[i][1]
        deal_n_over = re.sub(r'\n','',deal_n)
        tm = len(deal_n_over)#这里面那个函数名我忘记了
        #print a[i][0]
        #print tm
        print('%s\nTM:==>%s'%(a[i][0],tm))#这个是Python输出格式
#--------------------
#sqlite3
#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

import os,sqlite3
db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)
try:
    conn = sqlite3.connect('db_file')
    cursor = conn.cursor()
    sql_create = """create table report (id varchar(20) primary key, name varchar(20),score int)"""
    sql_insert = """insert into report (id, name, score) values ('A-001', 'Michael',98),
    ('A-002', 'Oocarain',56),
    ('A-003', 'Frozotol',82)"""
    cursor.execute(sql_create)
    cursor.execute(sql_insert)
    print('input success')
except:
    print('input error')
finally:
    cursor.close()
    conn.commit()
    conn.close()
    print('-'*10,'INPUT OVER','-'*10)

def get_score_in(low,high):
    try:
        conn = sqlite3.connect('db_file')
        cursor = conn.cursor()
        #sql_select = """select name from report where score betwen ? and ? order by name ,(low,high)"""
        cursor.execute('select name from report where score between ? and ? order by score',(low,high))
        values = cursor.fetchall()
        def f(x):
            return x[0]
        return list(map(f,values))
    except:
        print('read error')
    finally:
         cursor.close()
         conn.close()
         print('-'*10,'RUN','-'*10)
print('20-70:',get_score_in(20,70))
print('60-85:',get_score_in(60,85))
print('20-100:',get_score_in(20,100))

#------------------------------------
#使用sqlalchemy
#=================初始化======================
# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'
    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://oocarain:123456@localhost:3306/pytest')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()
#================插入数据======================

# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
#===============查询数据=======================
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()

#-------------查询---------
import pymysql

db = pymysql.connect('localhost','oocarain','123456','pytest')
cursor = db.cursor()
sql_select = "select * from employee where income between %d and %d " % \
 (2000,3000)

cursor = db.cursor()

try:
   # 执行SQL语句
   cursor.execute(sql_select)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
       # 打印结果
      print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income ))
except:
   print ("Error: unable to fecth data")

# 关闭数据库连接
db.close()


#-------------------------------
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
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

def printUnivList(ulist,num):
    tpl = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tpl.format('排名','学校名称','总分',chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tpl.format(u[0],u[1],u[2],chr(12288)))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLTEXT(url)
    fillUniverList(uinfo,html)
    printUnivList(uinfo,20) #print tweteen university rank data
main()
#-----------------------------------------
