### windows 系统下命令行运行.py脚本文件 ###
>1.window7系统的话，推荐使用系统自带的Powershell,个人觉得这个比DOS命令行要好用，开始菜单搜索即可找到。

>2.记得切换到脚本文件所在的路径

>3.使用 python xxx.py运行脚本文件

>4.补充：流重定向（stream redirection）
>
>python xxx.py > abc.txt    (将脚本运行结果输出到abc.txt文本中)

附图：
![pypowershell](/md_pics/pypowershell1.png)
运行在不同路径下的.py脚本：
![pypowershell2](/md_pics/pypowershell2.png)

---	
1/1/2017 6:09:56 PM 	

**Win powershell 调用Python脚本里面的函数：**	

![module1](/md_pics/module2.png)	

![module1](/md_pics/module1.png)		

---	
1/12/2017 8:47:17 PM Frozoto1	

### 一不注意缩进就出错 ###

![suojin](/md_pics/pysuojin.png)

### Sublime Text3 REPL 定义函数与使用自定义函数 ###
![fun](/md_pics/pyhanshu1.png)	

我们不可以直接在脚本中定义完函数然后就直接函数名加上参数使用，下面就是错误示例：

![fun2](/md_pics/pyhanshu2.png)	

---	
1/13/2017 10:01:53 PM Frozoto1

## 鼓捣一下Ubuntu16.04 下Sublime Text3  ##

### 1.安装 	

[官网](http://www.sublimetext.com/3)下载.dbe安装包	
	
命令行安装	

	#dpkg -i xxxx.dbe

安装完成在命令行界面输入subl就可以打开了

### 2.激活 ###
在标题栏的help里面可以找到要输入license key的地方粘贴下面的key可以激活	
	
(这个购买的话折合人民币应该有450块钱左右吧，不过真的值这个价钱，不过我现在学生党也不富裕，就用着吧，不激活也可以用的，没有特别大的影响)

**下面是Sublime Text3 的 license key**
> Michael Barnes

> Single User License
> 
> EA7E-821385
> 
> 8A353C41 872A0D5C DF9B2950 AFF6F667
> 
> C458EA6D 8EA3C286 98D1D650 131A97AB
> 
> AA919AEC EF20E143 B361B1E7 4C8B7F04
> 
> B085E65E 2F5F5360 8489D422 FB8FC1AA
> 
> 93F6323C FD7F7544 3F39C318 D95E6480
> 
> FCCC7561 8A4A1741 68FA4223 ADCEDE07
> 
> 200C25BE DBBC4855 C4CFB774 C5EC138C
> 
> 0FEC1CEF D9DCECEC D3A5DAD1 01316C36

### 3.安装Package control ###
	
[安装代码官网获取](https://packagecontrol.io/installation)	

ctrl+`打开console,粘贴代码，Enter	

### 4.用Package Control安装其他插件  ###
	

ctrl+shift+p打开Package Control	


---	

1/14/2017 1:23:14 PM 

### windows下 通过pip3安装模块 ###

![pip3_win](/md_pics/win_pip3.png)



---


1/16/2017 11:36:51 AM Frozoto1

### 关于Python下的模块问题 ###

首先[Python官方手册-模块](http://www.pythondoc.com/pythontutorial3/modules.html)关于模块给出了说明简单的说明,下面是对模块的简单测试，说明一些问题：

1.一个起始的模块中定义了两个函数，之后又增加了一个函数用以验证模块的加载
![一个简单的模块](/md_pics/module0.png)

2.在powershell中直接使用模块名会出现什么效果

![module3](/md_pics/module3.png)

	No module named 'caogao' #提示我们没有叫caogao的模块
这个是因为我们当前的路径为C:\Users\Administrator,这个路径下面没有叫caogao的某块，所以需要切换路径：

![module4](/md_pics/module4.png)

这个时候是成功的了

3.下面我们在前面提到的模块中继续添加一个函数，然后调用一下这个函数：

![module5](/md_pics/module5.png)

	module 'caogao' has no attribute 'ceshi' #错误提示

这是什么原因呢？

原来是这样的
> Note：
> 
> 出于性能考虑，每个模块在每个解释器会话中只导入一遍。因此，如果你修改了你的模块，需要重启解释器；或者，如果你就是想交互式的测试这么一个模块，可以用 imp.reload() 重新加载，例如 import imp; imp.reload(modulename)。

下面我们测试一下：

![module6](/md_pics/module6.png)

**Success！！！**

**进一步地，我们来看一下**


---

2/15/2017 9:12:49 PM 

### Python与正则表达式 ###

这周在Python中遇到了正则表达式的一些问题，故深度学习了一下，下面是学习过程中参考的内容，和遇到的一些问题
参考链接：
[python正则表达式指南](http://www.code123.cc/255.html)

参考书目：
《Python核心编程》(第三版)

参考文章(百度云链接) :
[python正则表达式](http://pan.baidu.com/s/1pKZIcT9)

Python通过re模块来支持正则表达式。下面是对Python正则表达式的一些总结

1.group()与groups()

group() 返回整个匹配对象

group(num) 返回特定的子组

groups() 返回一个包含唯一会或者全部子组的**元组**，如果没有子组则返回空元组

示例：

    Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> import re
    >>> m = re.match(r'(\w\w\w)-(\d\d\d)','car-123')
    >>> m.group()
    'car-123'
    >>> m.group(1)
    'car'
    >>> m.group(2)
    '123'
    >>> m.groups()
    ('car', '123')
    >>> k = re.match('abc','abc')
    >>> k.group()
    'abc'
    >>> k.groups()
    ()
    >>> 

2.\b 与 \B

\bthe 匹配以the开始的字符串

\Bthe 包含但是不以the作为起始的字符串

示例：
    
    >>> import re
    >>> m = re.search(r'\bthe','sds the fsf')
    >>> if m is not None:m.group()
    ... 
    'the'
    >>> m = re.search(r'\bthe','sdsthe fsf')
    >>> if m is not None:m.group()
    ... 
    >>> m = re.search(r'\bthe','sds thefsf')
    >>> if m is not None:m.group()
    ... 
    'the'
    >>> m = re.search(r'\Bthe','sdsthe fsf')
    >>> if m is not None:m.group()
    ... 
    'the'
    >>> m = re.search(r'\Bthe','sdseht fsf')
    >>> if m is not None:m.group()
    ... 
    >>> 
    
3.findall() 与 finditer()

findall()查询字符串中某个pattern全部的非重复出现情况

findall() 总是返回列表

finditer() 返回的是一个迭代器

示例：

	>>> s = 'This is that you like and I named it TH'
    >>> re.findall('car','car oocarain carcar hicar carhi')
    ['car', 'car', 'car', 'car', 'car', 'car']
    >>> re.findall(r'(th\w*)',s,re.I)
	['This', 'that', 'TH']
	>>> re.findall(r'(th\w*).+(th\w*).+(th\w*)',s,re.I)
	[('This', 'that', 'TH')]
	>>> [g.group(1) for g in re.finditer(r'(th\w*)',s,re.I)]
    ['This', 'that', 'TH']
    >>> 

4.sub 与 subn
两者用法都是一样的，只是：

sub 返回替换后的字符串

subn 返回一个元组，元组里面包含替换后的字符串和替换总数的数字

示例：

    >>> re.sub(r'(\w)-(\w)',r'\2-\1','a-b')
    'b-a'
    >>> re.subn(r'(\w)-(\w)',r'\2-\1','a-b')
    ('b-a', 1)
    >>> re.sub(r'[oc]','x','oocarain')
    'xxxarain'
    >>> re.subn(r'[oc]','x','oocarain')
    ('xxxarain', 3)
    #将日期表示法MM/DD/YY --> DD/MM/YY
	>>> re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})',r'\2/\1/\3','3/20/1994')


5.一个很好的例子说明re模块中Match的一些属性
    
    import re
    m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
    
    print ("m.string:", m.string)
    print ("m.re:", m.re)
    print ("m.pos:", m.pos)
    print ("m.endpos:", m.endpos)
    print ("m.lastindex:", m.lastindex)
    print ("m.lastgroup:", m.lastgroup)
    
    print ("m.group(1,2):", m.group(1, 2))
    print ("m.groups():", m.groups())
    print ("m.groupdict():", m.groupdict())
    print ("m.start(2):", m.start(2))
    print ("m.end(2):", m.end(2))
    print ("m.span(1):", m.span(1))
    print (r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3'))
    
    #输出
    #m.string: hello world!
    #m.re: re.compile('(\\w+) (\\w+)(?P<sign>.*)')
    #m.pos: 0
    #m.endpos: 12
    #m.lastindex: 3
    #m.lastgroup: sign
    #m.group(1,2): ('hello', 'world')
    #m.groups(): ('hello', 'world', '!')
    #m.groupdict(): {'sign': '!'}
    #m.start(2): 6
    #m.end(2): 11
    #m.span(1): (0, 5)
    #m.expand(r'\2 \1\3'): world hello!

6.扩展表示法：(?:...)    

    import re
    
    #(?:)
    pattern1 = re.compile(r'(?:\w+\.jpg)')
    #以jpg为结尾的字符串,匹配不保存下来
    
    #(?#)
    pattern2 = re.compile(r'\w{2}(?# This is a test)[a-f]')
    #加注释信息
    
    #(?=)
    pattern3 = re.compile(r'\w{8}(?=\.top)')
    #一个字符串后面跟.top才做匹配操作
    
    #(?!)
    pattern4 = re.compile(r'\w{8}(?!\.com)')
    #字符串后面不跟着.com才做匹配操作
    
    #(?<=)
    pattern5 = re.compile(r'(?<=0527-)\d{8}')
    #字符串之前为'0527-'才做匹配
    
    #(?<!)
    pattern6 = re.compile(r'(?<!192\.168\.)\.\d{1,2}\.\d{1,2}')
    #字符串之前不是'192.168.'才做匹配操作
    
    #(?(1)y|x)
    pattern7 = re.compile(r'(?:(x)|y)(?(1)y|x)')
    #匹配组1(\1)存在就与y匹配，否则就与x匹配
    
    test = input("Test string(use':'split the string):")
    #you can input:abc.jpg:oka:oocarain.top:oocarain:0527-84734123:196.172.0.1:xy
    list_test = test.split(':')
    dict_test = {}
    for i in range(7):
    k = 'test'+str(i+1)
    dict_test[k] = list_test[i]
    
 
    m1 = pattern1.match(dict_test['test1'])
    m2 = pattern2.match(dict_test['test2'])
    m3 = pattern3.match(dict_test['test3'])
    m4 = pattern4.match(dict_test['test4'])
    m5 = pattern5.findall(dict_test['test5']) #此处不可以使用match()方法
    m6 = pattern6.findall(dict_test['test6']) #此处不可以使用match()方法
    m7 = pattern7.search(dict_test['test7'])   #此处不可以使用match()方法

    print('-'*20)
    
	#测试：
    print ('P1==>','m1.string:',m1.string,'m1.pos:',m1.pos)
    print ('P2==>','m2.string:',m2.string,'m1.pos:',m2.pos)
    print ('P3==>','m3.string:',m3.string,'m1.pos:',m3.pos)
    print ('P4==>','m4.string:',m4.string,'m1.pos:',m4.pos)
    print ('P5==>',m5)
    print ('P6==>',m6)
    print ('P7==>',bool(m7))
	#输出：
    --------------------
    P1==> m1.string: abc.jpg m1.pos: 0
    P2==> m2.string: oka m1.pos: 0
    P3==> m3.string: oocarain.top m1.pos: 0
    P4==> m4.string: oocarain m1.pos: 0
    P5==> ['84734123']
    P6==> ['.0.1']
    P7==> True

---

2/20/2017 10:00:04 AM 

### Python之上下文管理器 ###

[参考博客](https://my.oschina.net/935572630/blog/397251)

[contextlib](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001478651770626de401ff1c0d94f379774cabd842222ff000)

上下文管理器的任务是：代码块执行前准备，代码块执行后收拾

1.使用上下文管理器

问题：用open()与close()读写文本会出现异常，比如磁盘写满，此时close()无法被执行，文件资源没有被关闭，怎么办，可以使用下面代码

	try:
		...
		...
	finally:
		...
解此问题，但是这样真是很丑陋和麻烦的事

解决：上面代码可以简化为

	with open('path\to\file','r') as f:
		f.read()

这样就不必担心资源没有关闭了



> 深入一点：
> 
> 1.并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。
> 
> 2.with语句的作用类似于try-finally，提供一种上下文机制。
> 
> 3.as指代了从open()函数返回的内容，并把它赋给了新值f,在后文的自定义上下文管理器中我们会知道as指代的就是__enter__中函数的返回

2.自定义上下文管理器

问：那么如何实现上下文管理呢？

答：实现上下文管理需要\__enter\__和\__exit\__这两个方法
	
下面以一个class类实现这两个方法

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

	#==========输出=============

		------------------ BEGAIN ------------------
		hello: 0
		hello: 1
		hello: 2
		hello: 3
		hello: 4
		hello: 5
		hello: 6
		hello: 7
		hello: 8
		hello: 9
		-------------------- END --------------------

3.@contextmanager

觉得写\__enter__ 和 \__exit__还是很麻烦，使用Pyhthon自带模块contextlib中的contextmanager。@contextmanager让我们通过编写generator来简化上下文管理。

示例1：

    from contextlib import contextmanager

    class f1(object):
    	def __init__(self,name):
    		self.name = name
    	def logname(self):
    		print('input your true name: %s'% self.name)
   
    @contextmanager

    def login(name):
    	print('loging...')
    	fc = f1(name)
    	yield fc
    	print('login success')

    with login('oocarain') as lg:
    	lg.logname()

	#=======输出======
	loging...
	input your true name: 
		oocarain
	login success

示例2：

	from contextlib import contextmanager

	@contextmanager
	def f2():
    	print('input password ')
    	yield
    	print('login success')
	with f2():
    	print('123456')

	#=====输出========
	input password 
	123456
	login success
这样的作用是，在代码执行前，执行特定的代码，with下的是我们想要执行的代码，with前的函数就是对其上下文的修饰。@contextmanager这个decorator接受一个generator，用yield语句把with ... as var变量输出出去，然后，with语句就可以正常地工作了。
上面示例2的执行顺序是：

>1.with语句首先执行yield之前的语句
> 
>2.yield调用会执行with语句内部的所有语句
> 
>3.最后执行yield之后的语句

插：如果一个对象没有实现上下文，我们就不能把它用于with语句。

4.用closing()把任意对象变为上下文对象，使其支持with语句

示例：

	from contextlib import closing
	from urllib.request import urlopen

	with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
