##R中一些帮助函数##
#*****************************************#
#?foo 查看函数foo的帮助文档
#??foo 以foo为关键字搜索本地帮助文档
#example("foo") 函数foo的使用示例
#apropos("foo",mode="function) 列出，名称中含有foo的所有函数

##管理R工作空间的函数##
#****************************************#
#getwd() 显示当前的工作目录
#setwd("D:/R working dir") 修改当前工作目录为D:/R working dir
#ls()列出当前工作空间中的对象
#q()退出R

##第2章创建数据集
#****************************************************************************#
#数据结构 ，R中存储数据的对象类型有：标量，向量，矩阵，数组，数据框，列表
#标量 ，只含一个元素的向量，例如m <- 3
#向量 ，c()
#矩阵 ，是一个二维数组
#       mymatrix <- matrix(vector,nrow=number_of_rows,ncol=number_of_cols,byrow= logical_value,
#                         dimnames=list(char_vector_rownames,char_vector_colnames))
#       默认情况下，byrow=FALSE,即按列填充
#e.g.  
rnames <- c("a","b","c","d")
cnames <- c("A","B","C","D","E")
vector <- 1:20
y <- matrix(vector,nrow = 4,ncol=5,byrow = TRUE,dimnames = list(rnames,cnames))
y

#数组 ，与矩阵类似，但是维度可以大于2
#myarray <- array(vector,dimensions,dimnames) #dimensions 是一个数值型向量，给出了各个维度下标的最大值
#e.g.
dim1 <- c("A1","A2")
dim2 <- c("B1","B2","B3")
dim3 <- c("C1","C2","C3","C4")
z <- array(1:24,c(2,3,4),dimnames = list(dim1,dim2,dim3))  #2行3列4层
z
#数据框 （用于不同的列包含不同的数据），通过函数data.frame()创建
#mydata <- data.frame(col1,col2,col3...) 列向量col1,col2,col3...可为任何类型（数值，字符，逻辑）
#列名称由函数names()指定

#attach() ,detach() ,with()
# 特殊赋值符 <<-，可将对象保存到with（）之外的全局环境中
#实例标识符（行名）可以通过函数row.names指定

#名义型变量和有序型变量在R中称为因子（factor）
#函数factor()以一个整数向量的形式储存类别值
#e.g. 
diabetes <- c("Type1","Type2","Type1","Type1")
diabetes <- factor(diabetes)  #将会使此向量储存为（1，2，1，1） ,内部关联为1=Type1,2=Type2
#要表示有序型向量，需要为factor()指定参数ordered=TRUE
#levels覆盖默认排序levels=c(...)

#str(object) 显示对象的结构
#summary(object) 显示对象的统计概要

#列表（list） mylist <- list(object1,object2,...) 这里的对象可以是前面的任何结构
#为列表中的对象命名 mylist <- list (name1=object1,name2=object2...)
#e.g.
a <- "My first list"
b <- c(10,2,3,5,6)
c <- matrix(1:10,nrow = 5)
d <- c("one","two","three")
mylist <- list(title=a,ages=b,c,d)
mylist
#数据的输入 p31

#处理数据对象的实用函数
#str(object) 显示对象的结构
#length(object) 显示对象中元素或是成分的数量
#ls() 显示当前的对象列表
#rm(object,object..) 删除一个或多个对象
#fix(object) 直接编辑对象

#第3章 图形初阶

#通过代码保存图形，将绘图语句夹在开启和关闭目标图形设备的语句之间即可
#e.g.
pdf("mygraph.pdf")  #开启   （mygraph.pdf文件与.R文件在同一个文件夹下）
attach(mtcars)
plot(wt,mpg)
abline(lm(mpg~wt))
title("Regression of MPG on Weight")
detach(mtcars)
dev.off()          #结束

#dev.new() ,创建一个新图形之前打开一个新的窗口、
































