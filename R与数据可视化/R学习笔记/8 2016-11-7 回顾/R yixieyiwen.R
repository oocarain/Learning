#选入观测值与subset()函数
somdata <- data.frame()
fix(somdata)
newdata <-somdata[1:3,]
bdata <- somdata[which(somdata$gender=="M" & somdata$age >30),]
bdata
nndata <-subset(somdata,age>=35 | age<24,select = c(q1,q2,q3,q4))
nndata

x <- nrow(somdata)   #数据框有多少行
x
y <- ncol(somdata)   #数据框有多少列
y 

#随机观测值产生
mysample <- somdata[sample(1:5,3,replace=FALSE),]
mysample

##统计函数
#分位点的一个例子
k <- c(1,2,3,4,2,3,5,6,1,2,5,6,8,4,3,6,9)
L <- quantile(k,c(.6,.8))
L
#滞后分位差
lol <- c(1,5,9,15,25,28)
zhfwc <-diff(lol)  #默认lag=1    ，lag指的是滞后的项数
zhfwc
  #-修改一下lag看一下效果
happy <- c(1,5,9,15,25,28)
zhihou <-diff(happy,lag = 2)  #默认lag=1
zhihou
#数据对象中心化或标准化
  #下面应到的标准化方法是z-score标准化方法，基于均值和标准差
  #新数据=（原数据-均值）/标准差
reportdata <- data.frame()
fix(reportdata)
aft <- scale(reportdata[2:4],center = TRUE,scale = TRUE)
aft
fix(reportdata)
cai <- scale(reportdata[2:4],center = TRUE,scale = TRUE)
cai
ds <- sd(reportdata$english)
ds
    #基于不同均值与标准差，标准化数据
what <- scale(reportdata$english)*1.14 + 75
what

#
x <- pretty(c(-3,3),30)
y <- dnorm(x)
plot(x,y,
     type = "l",
     xlab = "Normal Deviate",
     ylab = "Density",
     yaxs="r")   #"r"与"i"的区别

#输出前十个观测值 --- head (mydata,n=10)
now <- sub("\\s",".","hello world \\s")  #默认fixed=FALSE,即pattern为正则表达式
now

qq <- strsplit("abcdef","")
qq

qiege <- cut(1:100,8,ordered_result = TRUE)

#type= "p "  在图形中数据显示为点
#type= "l "  在图形中数据显示为线
#type= "b "  在图形中数据显示为点和连接线
#type= "o "  在图形中数据点覆盖在线上
#type= "h "  在图形中数据显示为从点到x轴的垂直线
#type= "s "  在图形中数据显示为阶梯图
#type= "n "  在图形中数据不显示

layout(matrix(c(1,2,3,4,5,6,7,7),4,2,byrow = TRUE))
plot(1:30,type="l",main="type=l ")
plot(1:30,type="p", main=" type=p ")
plot(1:30,type="b" ,main=" type=b ")
plot(1:30,type="o", main=" type=o ")
plot(1:30,type="h", main=" type=h ")
plot(1:30,type="s" ,main=" type=s ")
plot(1:30,type="n", main=" type=n ")



















