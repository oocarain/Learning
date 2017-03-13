## 记录MySQL学习过程遇到的问题 ##

系统：win32位 MySQL版本：5.7.17-log

Mysql语法对大小写不敏感，但是大写更容易看出

### 1.启动关闭MySQL服务 ###
1【开始菜单】搜索services.msc打开windows【服务管理器】，可以在此开启关闭MySQL服务。

2在cmd中使用命令：

	net start mysql #启动mysql服务
	net stop mysql	#关闭mysql服务
遇到net命令无法识别，如下：

![mark](http://ol8t44w0x.bkt.clouddn.com/blog/20170225/222723442.png)

这是环境变量没有配置的原因，究竟是哪一个文件的环境变量没有配置呢？

是C:\windows\system32\这个路径下的net.exe没有配置环境变量

现切换到这个路径下试一下可不可以使用net命令：

![mark](http://ol8t44w0x.bkt.clouddn.com/blog/20170225/223320505.png)

- 在Powershell需要使用

	.\net stop mysql

	 关闭服务。

- 在cmd中可以直接使用

	net start mysql

	启动服务

![mark](http://ol8t44w0x.bkt.clouddn.com/blog/20170225/223654386.png)

将c:\windows\system32添加到系统的Path中后：

![mark](http://ol8t44w0x.bkt.clouddn.com/blog/20170225/224147474.png)

成功！！！

---

2/27/2017 10:57:22 AM 

### 2.MySQL添加用户并授权 ###

登录root账户后执行下面操作：

1、创建用户,名字为oocarain,密码为123456

	mysql>create user oocarain identified by '123456';

2、创建名字为pytest的数据库

	mysql>create database pytest;

3、授予pytest数据库的所有权限给oocarain用户：

	mysql>grant all on pytest.* to oocarain

PS:如果第3步授权失败，可以退出root账户，并重新登录，再次授权；

4.完成用户的创建后，请记得刷新系统权限表

	mysql>flush privileges

### 3.数据库基本操作 ###

1.查看当前所有存在的数据库

	mysql>SHOW DATABASES;
2.创建一个新的数据库

	mysql>CREATE DATABASE database_name
3.删除数据库

	mysql>DROP DATABASE database_name
4.查看创建数据库的详细信息

	mysql>SHOW CREATE DATABASE database_name\G
(\G的会使输出的结果更规范，方面阅读)

5.使用一个数据库

	mysql>USE database_name
6.查看系统支持的存储引擎类型

	mysql>SHOW ENGINES\g
(在\g与\G在输出结果的格式上会有不一样，跟喜欢用\g)

### 4.数据表的基本操作 ###

1.创建数据表
建立一个名为test的表

![mark](http://ol8t44w0x.bkt.clouddn.com/blog/20170306/130611715.png)

>- primary key 主键约束
> 
> - not null 非空约束
> 
> - unique 唯一性约束
> 
> - default 默认约束
>
>- auto_increment 
>
>属性值自动增加（一个表只能有一个这样的约束，且该字段必须是主键的一部分）
>
> - 创建外键规则
> 
> CONSTRAINT <外键约束名> FOREIGN KEY(<字段名>) REFERENCES 主表名(<主键>)

补：test表设置的外键所联系的主表为tb_dept1,详细如下

![mark](http://ol8t44w0x.bkt.clouddn.com/blog/20170306/130912363.png)

2.查看数据表结构

	mysql>DESCRIBE table_name
简写：

	mysql>DESC table_name
![mark](http://ol8t44w0x.bkt.clouddn.com/blog/20170306/130734990.png)

查看表的详细信息：

	mysql>show create table table_name
注：
      
- NULL表示该列是否可以存储NULL值
- DEFAULT 表示该列是否有默认值
- Key 表示该列是否编制了索引。
	- PRI表示该列为主键的一部分
	- UNI表示该列为UNIQUE索引的一部分
	- MUL该列中某个给定值可以出现多次
	
3.修改数据表

MySQL使用ALTER TABLE语句修改表。

1.rename(修改表名)
	
	mysql>alter table 旧表名 rename 新表名
2.modify(修改字段类型，修改字段的排列位置)

	mysql>alter table tb_dept1 modify name varchar(30)
	#将tb_dept1表中的name字段类型修改为varchar(30)

	mysql>alter table tb_dept1 modify column3 varchar(12) first
	#将column1修改为标的第一个字段
	
	mysql>alter table tb_dept1 Modify column3 varchar(12) after location
	#将column3字段插入到location字段之后
3.change(修改表字段名,修改字段类型)

	mysql>alter table tb_dept1 change location loc varchar(60)
	#修改location字段名为loc
	mysql>alter table tb_dept1 change loc loc varchar(100)
	#修改loc字段类型为varchar(100)
4.add(添加字段）

- 无约束条件
	- mysql>alter table tb_dept1 add mangeerID int(10);
- 有约束条件
	- mysql>alter table tb_dept1 add column4 varchar(20) not null;
- 在第一列添加字段
	- mysql>alter table tb_dept1 add mangeerID2 int(10) first;
- 在指定列之后添加字段
	- mysql>alter table tb_dept1 add column5 int(10) after name
	
5.drop(删除字段,删除表的外键，删除数据表，删除数据库)

	mysql>alter table tb_dept1 drop column5;
	#删除column5字段

	mysql>alter table <表名> drop foreign key <外键约束名>;
	#删除外键

	mysql>drop table if exists tb_name1,tb_name2...tb_namen;
	#如果表tb_name1,tb_name2...tb_namen存在则将其删除
	#(如果主表被其他表关联，要删除这个主表首先要删除与其关联的外键)

	mysql>drop database database_name
	#删除数据库 
	

 429240967@qq.com