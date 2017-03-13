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
	#(注：add所有修改的文件，可以如下使用命令)
	git add .
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

![mark](http://ol8t44w0x.bkt.clouddn.com/blog/20170305/153534451.png)

> 9.生成SSH key
> 
	ssh-keygen -t rsa #rsa为指定算法

> 10.测试密钥是否添加成功
> 
	ssh -T git@github.com

> 11.关联本地库与远程库
> 
	git remote add origin git@github.com:oocarain/Learning.git

注：origin是给远程仓库起的名字

> 12.push推送到远程
> 
	git push origin master

> 13.pull将远程修改拉到本地
> 
	git pull origin master

> 14.git命令缩写修改
> 
	git config --global alias.co checkout # 别名
    git config --global alias.ci commit
    git config --global alias.st status
    git config --global alias.br branch
	git config --global alias.psm 'push origin master'
	git config --global alias.plm 'pull orig

将git log 的输出更适合阅读：

    git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%
    d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative"