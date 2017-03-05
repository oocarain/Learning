11/25/2016 4:00:14 PM    *by.cjw*
### 关于R语言版本升级一些内容###
>只需要在R console窗口下执行如下代码就可以了

	install.packages("installr")
	library(installr)
	updateR()

> 另外需要注意的是安装完后，会弹出几个交互的窗口，具体就是继承以前的安装包之类的很简单，看着点点点就可以个，另外就是若以前安装的包，没有在新版本中显示则可以将旧版本library文件夹里面的内容copy到新的版本library文件夹下。下面贴几张图

![R updata](/md_pics/update.png)	

![R升级](/md_pics/sp20161125_155955.png)

> 升级完成后新版本号在每次打开R的时候console最上面都有显示

### 修改R工作目录 ###
![changewd](/md_pics/changewd.png)
把新的工作目录copy覆盖起始位置路径即可		

- 注：以外发现此处插入的图片名称中是不能有空格的不然识别不了。

### REmap的安装与使用 ###
> console里面执行

	library(devtools)
	install_github('lchiffon/REmap')



- 注：出现问题，提示：没有安装curl包，所以还要先安装一下curl包，再次执行上面代码，成功安装。

![remap](/md_pics/remap.png)

> REmap是什么

![REmapwhat](/md_pics/remapwhat.png)
REmap的介绍和用法还可以参见[REmap发布，用R绘制百度迁徙图](http://www.xueqing.tv/cms/article/view/id/10)
这篇文章可以说是REmap的起始，现在的版本才0.3，看好它的发展。

3/5/2017 5:03:06 PM 
