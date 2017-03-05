#This is a review of learning git#

3/5/2017 11:16:46 AM 


> 1.初始化一个仓库
> 
	git init

> 2.查看当前仓库的状态
> 
	git status

> 3.向仓库中添加文件(filename根据实际替换)
> 
	git add filename

> 4.提交到
> 
	git commit -m '描述提交的信息' #-m参数和后面的消息用来描述本次提交的消息

> 5.查看日志
> 
	git log

>6.创建一个分支copy(copy是分支的名字)
> 
	git branch copy

> 7.切换到分支copy
> 
	git checkout copy

> 8.删除分支copy
> 
	git branch -d copy #git branch -D copy强行删除分支copy，如果copy分支没有合并到master的话

> 9.合并分支到master(执行合并操作要先切换到master分支)
> 
	git merge copy #将分支copy合并到master

### 遇到的问题 ###

Push到远程出现如下问题:

![mark](http://ol8t44w0x.bkt.clouddn.com/blog/20170305/153236729.png)

可以通过命令：

	$git push -f 
解决。


