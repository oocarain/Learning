### linux网络配置 ###

Linux 发行版本：Centos6.5

12/17/2016 9:27:12 AM 

![linux启用网卡](/md_pics/linuxnetconfig1.png)

>命令解析：
>
>su -	        进入根用户身份
>
>ifup etho      启用第一块网卡（eth是ethernet的缩写）
>   
>ifconnfig etho 查看eth0的配置信息

注：这样可以打开网络链接，但是每次进入都要这样可能会很不方便，所以下面修改一个参数即可

![修改onboot](/md_pics/changeonboot.png)

首先进入network-scripts文件夹
>cd/etc/sysconfig/network-scripts/

这时可以用**ls**命令看一下network-scripts文件夹下文件，上图ifcfg-eth0即使我们第一块网卡所在的文件，下面用**cat**命令看一下这个文件中的信息
>cat ifcfg-eth0

看到ONBOOT=no说明开机启动的时候网卡是处于关闭状态的，下面将no修改为yes即可

>vi ifcfg-eth0

>*通过vi编辑器修改文本内容*

再次查看ifcfg-eth0文本信息
>cat ifcfg-eth0

这时候显示ONBOOT=yes就表示修改好了，下次在此进入的时候就不用在配置网络了

---
### 网络测试命令 ###

![nettest1](/md_pics/nettest1.png)
下面是网络测试的一些命令

![nettest](/md_pics/testnet.png)

注：追踪显示路径的时候，***，表是对方不让追踪，试了一些网站域名，发现大部分都没法解析	

---
12/18/2016 8:46:01 PM 
### Linux解释器路径 ###
Linux自带Python解释器，若要获得解释器路径，则可以在shell中输入如下的命令:
>which python

即可显示解释器的路径，一般路径为:
>/usr/bin/python

---
12/18/2016 11:39:19 PM 
### VMware Linux与windows之间实现文件共享 ###
>**核心工具VMware Tools**


具体配置参考链接：	

[图解：如何在LINUX中安装VM-Tools](http://www.cnblogs.com/puresoul/p/3650233.html);	

[Linux VMware Tools安装步骤](http://blog.sina.com.cn/s/blog_74e94c8401017zl7.html)

[怎样设置虚拟机和主机文件共享](http://jingyan.baidu.com/article/6b1823095583c1ba58e159a8.html)

>三个分享的方法都很好，但是都会有一些细节没有说到位，所以，综合了上面三个方法，完成了VMware Tools工具的安装，这样就可以实现虚拟机与本机之间的文件共享了。

下面是一张展示图：

![VMware share with windows](/md_pics/VMware_share_file_with_windows.png)


---
12/20/2016 9:10:47 PM 

### Linux cp命令没你想的那么简单 ###
cp可以满足大部分的拷贝情况，文件的拷贝，目录的拷贝，将文件拷贝到其他目录...但是有一种情况cp却遇到了麻烦也就是将文件拷贝到来源于不同根分支的目录下，比如：
>将/home/oocarain/test/yellow/yellowstar 下的文件拷贝到

>/usr/games 目录下，可以注意到/home 与/usr是不同的，这时候就会出现下面的问题：

![copy文件到根目录下被禁止](/md_pics/cp1.png)

这是怎么回事呢？又该如何解决这个问题呢？	

因为我们的权限不够，不可以执行这样的操作，所以可以尝试下面的命令：

>sudo cp /home/oocarain/test/yellow/yellowstar /usr/games

这时候又会出现这样的提示：
>xxx is not in the sudoers file(xxx为用户名）

原来我们的用户还不是sudoer所以我们需要设置一下，下面介绍如何设置：

首先进入root用户
命令：	
>su -


（这里要输入跟用户密码，我多嘴了）	
下面执行，命令：	
>visudo

在打开的配置文件中，找到root ALL=(ALL) ALL，在下面添加一行
xxx ALL=(ALL) ALL 其中xxx是你要加入的用户名称,修改完成记得：wq,保存退出	
这样回到普通用户下，执行：	
>sudo cp /home/oocarain/test/yellow/yellowstar /usr

我们将会看到:	
![cp2](/md_pics/cp2.png)
由上图我们可以看到，这时候还是要输入用户密码的（没错我的用户名就是oocarain）,记得这里要输入的是用户密码不是root密码，之后就可以看到要拷贝的yellowstar这个文件已经在/usr目录下了（在这里拷贝到/usr/games 道理是一样的）	

---
12/21/2016 8:03:03 PM 
### Linux 空行过滤 ###
Linux在处理空行方面有许多方法，下面总结一下	

1.grep	
	
	grep . data.txt	

	grep -v '^$' data.txt	

	grep '[^$]' data.txt
2.awk	

    awk NF data.txt   # 这个也可以将空格、tab等组成的空行删掉。
	awk '!/^$/' data.txt	

3.sed	

	sed  '/^$/d' data.txt
	sed '/^\s*$/d' data.txt   #这个命令还可将完全空格、tab等组成的空行删掉。
	# The character class \s will match the whitespace characters <tab> and <space>.	

4.tr	

	tr -s '\n' < data.txt

---

### Centos6.5 下Python版本升级问题 ###

默认情况下Centos6.5下的Python是2.6.6版本的，如何将其升级到Python2.7版本呢，下面在百度上找了一篇经验分享，很不错，[点击前往](http://jingyan.baidu.com/article/7082dc1c6ad06ce40a89bdf2.html)

只不过在操作的时候有一步命令稍有不同，原文中的命令是：	
>tar.xz tar -xvf Python-2.7.8.tar

但是实际上我在使用的时候用的是下面的命令，因为上面的命令出了一点问题	
> tar -xvf Python-2.7.8.tar


若要升级到python3.5.2可以参考下面的博文[点击前往](http://www.cnblogs.com/nulige/archive/2016/11/01/6020271.html)	


这种升级保留了原来的版本，这样两个Python版本都可以使用了

### 拷贝文本到Linux shell ###
>
使用Linux shell 的时候不免会输入一下比较长的命令，但是如果已经有现成的命令了，我们不想输入，想把文本中的内容拷贝到shell中该怎么办呢？上网查了一下，发现个简单的办法，一般我会把要输入的命令放在一个文本中，cat这个文本，在命令行中显示，可以Tab一个命令行窗口，这样会比较方便，选中要输入的命令，然后切换到要执行命令的窗口，按下鼠标滚轴键，也就是所谓的中键

---
### Linux 图形界面和文本界面切换 ###

[原文连接](http://www.cnblogs.com/deepstone/p/3344430.html)


### Linux 基本命令--注销，关机，重启 ###

[印象笔记](https://www.evernote.com/shard/s316/nl/156547426/ddd220b2-8c57-4595-b81b-091889ea9453/)	

---
12/31/2016 3:06:17 PM 
### Linux 下从命令行打开某些格式文件 ###

**打开当前目录下.pdf文件**
>evince xxx.pdf


![linux打开pdf html](/md_pics/linuxopenpdf.png)	

打开其他目录下的pdf文件需要完整的路径		

**打开当前目录.html文件**	
>firefox xxx.html

也可以直接跟网址：	
>firefox www.163.com

**打开.png图片文件**	
>eog xxx.png    

eog 的意思是eye of gnome	

---
*补充一个Liunx gnome遇到的workspace问题*
	
关于gnome下面的任务栏：
![1](/md_pics/workspace.png)	

![2](/md_pics/workspace2.png)	

![3](/md_pics/workspace3.png)	

![4](/md_pics/workspace4.png)


---	
12/31/2016 8:32:24 PM 	

**Linux shell 中调用Python解释器，清屏问题：**	

> If you're on GNU/Linux (I think in Mac OS too) this should do the trick:
> 
> import os; os.system('clear')

---	
1/10/2017 6:55:21 PM   Frozoto1

### Ubuntu16.04 关于apt		

>[Ubuntu16.04 新特性](http://www.linuxidc.com/Linux/2016-04/130136.htm)


>[Linux软件包管理基本操作入门](http://www.linuxidc.com/Linux/2016-01/127958.htm)


---	
1/10/2017 9:05:15 PM  Frozoto1		

*时代在发展科学在进步，技术的更新真是日新月异*	

当我还在搜索虚拟机上的Ubuntu16.04如何与属主机实现文件共享，并且苦于一系列的安装与配置，并且到现在还没有解决最后一个问题，突然发现软件的设计早已人性化到，直接在不同窗口间拖拽就可以复制想要的内容了，这确实可以解决不少问题，虚拟机与宿主机之间的文件共享还是需要解决的。	

---		

从 Ubuntu 11.04 中首次发布 Unity 以来，它就一直被固定在系统左侧。但从 Ubuntu 16.04 开始，用户已经可以手动选择将 Unity 栏放在桌面左侧或是底部显示，目前还没办法将其移动到顶部或右侧，通过下面命令可以实现：		

	$gsettings set com.canonical.Unity.Launcher launcher-position Bottom	

---

2/10/2017 9:41:41 AM 

### linux 忘记用户密码和Root密码怎么办 ###

*不到一个月没有登录就把密码忘记了，忘记的很彻底，只能记得这个密码很简单很好记，但是怎么也想不起来了，无奈只好想其他办法了*

Linux发行版本：Ubuntu16.04

解决方法：[ubuntu 16.04忘记root密码的处理方法](http://www.linuxdiyf.com/linux/21513.html)

上面这篇博文说的很明白了但是有几点补充：

- 开机按Esc键可能不会出现文中出现的窗口，这时候可以尝试开机时长按shift键

- 文中说选择带recovery mode 的选项但是可能会有好几个，怎么办，一个个试一下，第一个不行就重新选择第二个...，问题的关键在于后面你可能找不到recovery nomodeset，故无法接着往后面进行设置了，所以运气好的第一个recovery mode 就可以，不行的话换下一个就可以了，一共也没几个

- 关于修改密码的小问题：

![passwd](/md_pics/passwd.jpg)

	#passwd    //修改Root密码
	#passwd username  //修改用户密码

---

2/23/2017 8:10:46 PM 

### primer3-py与Biopython模块的安装与使用 ###

Ubuntu16.04下
#### 简介 ####

**Primer3-py** is a Python-abstracted API for the popular Primer3 library. The intention is to provide a simple and reliable interface for automated oligo analysis and design.([Primer3教程文档](https://libnano.github.io/primer3-py/quickstart.html))

**Biopython**工程是一个使用Python来开发计算分子生物学工具的国际团体。[Biopython官网](http://www.biopython.org)为使用和研究生物信息学的开发者提供了一个在线的 资源库，包括模块、脚本以及一些基于Python的软件的网站链接。一般来讲，Biopython致力于通过创造高质量的和可重复利用的模块及 类，从而使得Python在生物信息学中的应用变得更加容易。(附：[Biopython中文官方教程](http://biopython-cn.readthedocs.io/zh_CN/latest/cn/chr01.html))

---

#### 正文 ####
> 插：一般安装一个Python第三方模块首先去[PyPI](https://pypi.python.org/pypi)(the Python Package Index)搜索一下这个模块，查看一下这个模块的文档，从中我们可以了解许多信息。
> 以Primer3-py这个模块为例：


![mark](http://ol8t44w0x.bkt.clouddn.com/blog/20170223/230924874.png)
上面给出简单的使用介绍，如何获得模块的更全面的教程文档呢？看下面：

![mark](http://ol8t44w0x.bkt.clouddn.com/blog/20170223/231413408.png)
根据上面给的链接我们很容易找到模块的教程文档，如下：

![mark](http://ol8t44w0x.bkt.clouddn.com/blog/20170223/231527984.png)

还需要注意一点，就是这个模块可能还依赖其他模块，注意最下面的信息

![mark](http://ol8t44w0x.bkt.clouddn.com/blog/20170223/231853546.png)
注：Ubuntu16.04应该默认安装了Python2.x与Python3.x两个版本

**安装：**

	$pip list #检查Python2.x下安装的模块
	$pip3 list #检查Python3.x下安装的模块

若是没有Cython我们在安装之前要先安装Cython

	$pip install Cython
或者使用：

	$sudo apt-get install Cython
之后安装primer3-py和Biopython就可以使用如下命令：

	$pip install primer3-py
	$pip install Biopython
(问题：尝试使用pip3安装发现出现错误，原因还不是很清楚，使用apt-get安装的模块默认会在python2中，而且python3是无法直接使用，此问题有待解决)

**检查是否安装成功：**
	
![mark](http://ol8t44w0x.bkt.clouddn.com/blog/20170223/233837125.png)

import模块，没有消息就是好消息，说明安装成功，可以使用了。但是都是在Python2.x下使用的所以写的Python3脚本还要修改。

**下面以批量计算引物的TM值为例说明Primer3的使用：**

Python脚本(tm.py)：

	#!/usr/bin/env python
    #-*- encoding: UTF-8 -*-
    
    #calculate primer TM
    
    import primer3
    import re
    with open('ceshi.txt','r') as f:
    	my_ncfile = f.read()
    	a = re.findall(r'(?m)(^>.+)\n(.+)',my_ncfile)
    	for i in range(len(a)):
    		deal_n = a[i][1]
    		deal_n_over = re.sub(r'\n','',deal_n)
    		tm = primer3.calcTm(deal_n_over)
    		print a[i][0]
    		print '==>TM:',tm
    		#print('%s==>%s'%(a[i][0],tm))#python3 output

ceshi.txt中的文本信息：

    >106 Os10g17770-MT1T2-BsF
    AATAATGGTCTCAGGCGTGATTCTTCCCACGCGCCA
    >107 Os10g17770-MT1T2-F0			
    GTGATTCTTCCCACGCGCCAGTTTTAGAGCTAGAAATAGC
    >108 Os10g17770-MT1T2-R0			
    GCCATCCACGCCTAGCAAACGCTTCTTGGTGCC
    >109 Os10g17770-MT1T2-BsR			
    ATTATTGGTCTCTAAACGCCATCCACGCCTAGCAAA
    >110 Os01g58400-MT1T2-BsF			
    AATAATGGTCTCAGGCGTGGAGACTAACGGGATGAC
    >111 Os01g58400-MT1T2-F0			
    GTGGAGACTAACGGGATGACGTTTTAGAGCTAGAAATAGC
    >112 Os01g58400-MT1T2-R0			
    TATAAGCTTCAGCCTGTGGCGCTTCTTGGTGCC
    >113 Os01g58400-MT1T2-BsR			
    ATTATTGGTCTCTAAATATAAGCTTCAGCCTGTGG
    >114 Os05g41795-MT1T2-BsF			
    AATAATGGTCTCAGGCGGAGCGCTCCCCGCCGCGGT
    >115 Os05g41795-MT1T2-F0			
    GGAGCGCTCCCCGCCGCGGTGTTTTAGAGCTAGAAATAGC
    116> Os05g41795-MT1T2-R0			
    TCGCTGAAACATTTCGAAGCGCTTCTTGGTGCC
    >117 Os05g41795-MT1T2-BsR			
    ATTATTGGTCTCTAAATCGCTGAAACATTTCGAAG
    >118Os12g40790-MT1T2-BsF			
    AATAATGGTCTCAGGCGTGCTCCCCTCGAGAAGCTT

测试输出：

	$python tm.py
	#=======结果======
	>106 Os10g17770-MT1T2-BsF
    ==>TM: 68.2353763987
    >107 Os10g17770-MT1T2-F0
    ==>TM: 65.6391739803
    >108 Os10g17770-MT1T2-R0
    ==>TM: 69.1687268949
    >109 Os10g17770-MT1T2-BsR
    ==>TM: 64.2105900142
    >110 Os01g58400-MT1T2-BsF
    ==>TM: 64.9158844065
    >111 Os01g58400-MT1T2-F0
    ==>TM: 63.5527409589
    >112 Os01g58400-MT1T2-R0
    ==>TM: 66.7110214975
    >113 Os01g58400-MT1T2-BsR
    ==>TM: 58.6007567219
    >114 Os05g41795-MT1T2-BsF
    ==>TM: 74.4647040804
    >115 Os05g41795-MT1T2-F0
    ==>TM: 71.3344494613
    >117 Os05g41795-MT1T2-BsR
    ==>TM: 58.4296500085
    >118Os12g40790-MT1T2-BsF
    ==>TM: 67.448341691

    