# Python3 学习之路   ---Frozoto1
---
12/12/2016 8:11:31 PM 
## 从Python tutorial学起 ##
[Python tutorial](http://www.pythondoc.com/pythontutorial3)是Python的入门指南，本链接指向的是Release:3.5.2 Date:	Oct 08, 2016（比较新的指南

前两章的内容在这里笔记省略，下面会从第三章开始，整理一些Python个人认为在书中需要注意的地方。	

### Python简介 ###
Python当计算器使用真是大材小用了，新手入门这里总结几条


	>>> 17/2
	8.5			
	>>> 17//2
	8			#整除
	>>> 1+2
	3
	>>> _*5
	15			#交互模式中，最近一个表达式的值赋给变量_ 
	>>> _-5
	10
	>>> round(5,2)
	5			#round函数保留小数点后位数，展示
	>>> round(3.1415926070521345,5)
	3.14159
	>>> round(3.00005,3)
	3.0
	>>> round(3.010005,3)
	3.01
下面是关于'''....''', \ , r'...',在输出中的用法	

   
	>>> print('''hello\
	ooocarain love
	cheng''')
	helloooocarain love
	cheng
	>>> print('''hello
	ooocarain love
	cheng''')
	hello
	ooocarain love
	cheng
	>>> print(r'C:\users\administration\desktop')
	C:\users\administration\desktop
	>>> 

字符串索引与切片

	
	>>> sport = 'football'
	>>> sport[0]
	'f'
	>>> sport[3]
	't'
	>>> sport[-1]
	'l'
	>>> sport[1:4]
	'oot'
	>>> sport[-5:-1]
	'tbal'
	>>> 

这里需要注意的是：切片包含起始的字符，不包含末尾的字符，所以我们可以这样用

	>>> sport[:3]+sport[3:]
	'football'
	>>> 

len()函数返回字符串长度

	>>> a_long_word = 'jsdjsidjsdnsndsjdiujfdjfudhfn jidfjfnnsjdj'
	>>> len(a_long_word)
	42
	>>> 
[字符串格式化](https://docs.python.org/3/library/stdtypes.html#str.format)
### 列表 ###
列表支持索引		

---
1/1/2017 11:24:46 PM 

### 函数接口 ###

此部分参考[廖雪峰的官方网站](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000)

**位置参数**	
>基于参数的不同位置，传递对应的参数给函数
>	

**默认参数**
>给其中的位置参数一个默认的值，这样好处是，如果大部分情况都是默认值，那么我们就不用再输入默认值了，还可以防止我们遗漏参数，这时候用的就是默认的值，从而避免程序出错，另外，默认参数要放在后面，默认参数必须指向不变对象

**可变参数**
> 传入参数的个数是可变的（0个或是任一个参数），参数接受一个元组--tuple


> 我们常常输入的参数是不固定的，所以我们需要把要输入的参数整合为一个list或是tuple然后传进函数，这样很麻烦，所以下面就产生了可变参数，为了更好的传入可变参数

定义一个普通参数的函数：		

	def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
函数调用：

	>>> calc([1, 2, 3])
	14
	>>> calc((1, 3, 5, 7))
	84
定义一个含可变参数的函数：	

	def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
定义一个可变参数仅仅在参数前面加一个*(星号)		

函数调用：	

	>>> calc(1, 2)
	5
	>>> calc()
	0
**关键字参数**	
> 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。示例：

    def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

**命名关键字参数**
> 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数，至于传入了那些要做内部检查，有时我们要限制关键字参数的名字，这时候就可以用命名关键字参数。示例：

    def person(name, age, *, city, job):
    print(name, age, city, job)

与关键字参数不同，命名关键字参数需要用特殊字符*（星号）隔开，后面的参数为命名关键字参数

注：如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了

    def person(name, age, *args, city, job):
    print(name, age, args, city, job)

**参数组合**	
> 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。（补充一下，命名关键字可以有缺省值，从而简化调用）


对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。	

至此。1/12/2017 2:27:57 PM Frozoto1 整理

---		

2/10/2017 10:22:49 PM 

### Python内置的 JSON模块 ###

Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。

[link](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143192607210600a668b5112e4a979dd20e4661cc9c97000)

	>>> import json 
    >>> a = '[1,2,3,4,5,6]'
    >>> a
    '[1,2,3,4,5,6]'
    >>> json_a = json.loads(a)
    >>> json_a
    [1, 2, 3, 4, 5, 6]
    >>> 







