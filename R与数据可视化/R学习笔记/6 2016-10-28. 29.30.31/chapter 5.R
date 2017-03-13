#2016/10/28
#chapter 5 高级数据管理
#############################
x <- pretty(c(-3,3),30)
y <- dnorm(x)
plot(x,y,type = "l",xlab="Normal Deviate",ylab="Density",yaxs="i")
############################
pnorm (1.95)          #左侧正态分布曲线面积
qnorm(.9,mean = 500,sd=100)#均值500，标准差为100的正态分布的0.9分位点的值
rnorm(50,mean = 50,sd=10)#生成50个均值为50，标准差为10的正太随机数
runif(5) #0-1之间生成5个服从均匀分布的伪随机数
set.seed(1234)  #z这里面的参数1234就是个名字而已，没什么意义，换成其他的也行
runif(3)
set.seed(1234)  #两个相同的种子名字表示下面的随机数从上面重复来
runif(3)       #两个种子之间只产生一个随机数组，所以下面只有第一组随机数和
runif(3)       #-上面的相同，其余的随机数组都不同
runif(3)
runif(3)
runif(3)

#下面是一个小测试
#1
set.seed(1)
runif(3)
runif(3)
runif(3)
set.seed(1)
runif(3) 
runif(3)
runif(3)       #前三组随机数和上面三组随机数对应相同
runif(3)       #第四组随机数和上面的不同
#2
set.seed(2)      #产生5组随机数
runif(3)
runif(3)
set.seed(3)
runif(3)
runif(3)
runif(3)




#2016-10-29
#接着第五章内容

#生成多元正态数据
options(digits = 3)
set.seed(1234)

mean<- c(230.7,146.7,3.6)
sigma<-matrix(c(15360.8,6721.2,-47.1,
                672.2,4700.9,-16.5,
                -47.1,-16.5,0.3),nrow = 3,ncol = 3)

mydata <- mvrnorm(100,mean,sigma)
mydata <- as.data.frame(mydata)
names(mydata) <- c("y","x1","x2")
dim(mydata)
head(mydata,n=10)

#字符处理函数
x <- c("asd","sdsfsfs","sdes")
nchar(x)
length(x)
nchar(x[2])

y <- "abcdefghij"
m <- substr(y,3,5)   #提取
m #m value
y #y value
substr(y,2,4) <- "111" #查找替换
y #y value

paste(c("a","b","c"),1:3,sep="-")
paste("x",1:3,sep="")
paste("Today is",date())

s <- strsplit(c("oocarain","javen","superpaprika"),"")
s
#更多见p90
momo <-seq(1,10,2)#1-10之间步长为2，生成一个序列
momo

cop <- rep(1:3,2)#将1：3之间的数重复2次，123123
cop

#p93 代码清单5-6 一个综合问题的解决、
############################################
options(digits = 2)   #限制输出的小数点后的位数

students <- c("John Davis","Angela Williams","Bullwinkle Moose",
              "David Jones","Janice Markhammer","Cheryl Cushing",
              "Reuven Ytzxds","Greg Knol","Jonel England","Mary Ray")
math <- c(502,600,412,358,495,512,410,625,573,522)
science <- c(95,99,80,82,75,85,80,95,89,86)
english <- c(25,22,18,15,20,28,15,30,27,18)
roster <- data.frame(students,math,science,english,stringsAsFactors = FALSE) #创建一个名为roster的数据框

zonghe <- scale(roster[,2:4])  #用scale()函数将数据标准化 p85  ?如何标准化的?
score <- apply(zonghe, 1, mean) #对标准化后的数据按行求均值
roster <- cbind(roster,score)   #将score列数据添加到roster数据框中

y <- quantile(score,c(.8,.6,.4,.2)) #输出学生得分的百分位数，即将成绩大于80%的临界分数给y,一次的60%...
y #这行用来看各等级临界点score的值
roster$grade[score >=y[1]] <- "A"              #将学生乘积按百分位数重编码，在数据框中添加grade变量
roster$grade[score >=y[2] & score<y[1]] <- "B"#
roster$grade[score >=y[3] & score<y[2]] <- "C"#
roster$grade[score >=y[4] & score<y[3]] <- "D"#
roster$grade[score<y[4]] <- "E"

name <- strsplit(roster$students," ")      #将学生姓名按空格拆开
lastname <- sapply(name,"[",2)             # "[" 是提取对象某一部分的函数，这里提取name中的第二个元素
firstname <- sapply(name, "[",1)           #
roster <- cbind(firstname,lastname,roster[,-1]) #将姓与名添加到数据框，并删除students变量
roster <- roster[order(lastname,firstname),]    # 用order函数按lastername 和 firstname 进行排序
roster

###########################################

#2016-10-30
#5.4控制流



#2016-10-31
#整合数据
options(digits=3)
attach(mtcars)
aggdata <- aggregate(mtcars,by=list(Group.cyl=cyl,Group.gears=gear),FUN = mean,na.rm=TRUE)
aggdata

#reshape包
#融合melt()

mydata <- data.frame()
fix(mydata)
library(reshape2)
md<- melt(mydata,id=(c("id","time")))
md
kkk <- cast(md,id~variable,mean)
kkk
#重铸cast()  cast(mel.mydata,formula,FUN)
#mel.mydata-已融合的数据，formula-想要的最终结果，FUN-可选的数据整合函数

























