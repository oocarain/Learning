#par(mfrow=c(2,2))
opar <- par(no.readonly = TRUE)
par(mfrow=c(2,2))
slices <- c(10,12,4,16,8)
lbls <- c("USa","UK","AUSTR","GERM","France")
pie(slices,labels = lbls,main = "simple pie")

pct <- round(slices/sum(slices)*100)
lbls2 <- paste(lbls," ",pct,"%",sep = "")
pie(slices,labels = lbls2, col=rainbow(length(lbls2)),
    main="Percentage pie")

library(plotrix )
pie3D(slices,labels=lbls,explode=0.01,main="3D Pie Chart")
                #explode 在此处有打碎的含义，即各个扇形块之间有空隙
mytable <- table(state.region)
lbls3 <- paste(names(mytable),"\n",mytable,sep="")
pie(mytable,labels = lbls3,main = "Pie Chart from a Table\n (w s s)")
par(opar)

#扇形图
changchun<- c(25,12,4,6,18)
names <- c("oocarain","wayneHU","fengLi","chunxie","wenBO")
fan.plot(changchun,labels = names,main = "Number of fans ",
         col=rainbow(length(names)))

#直方图
lpar <- par(no.readonly = TRUE)
par(mfrow=c(2,2))

hist(mtcars$mpg) #简单直方图

hist(mtcars$mpg,
     breaks = 12,
     col="green",
     xlab="Miles Per Gallon",
     main =" Colored hist with 12 bins") #默认freq=TRUE,即用频数绘图

hist(mtcars$mpg,
     freq = FALSE,
     breaks = 12,
     col="red",
     main="Hist rug plot density curve")
rug(jitter(mtcars$mpg))
lines(density(mtcars$mpg),col="blue",lwd=2)
box()   #在外围加上一个盒型
                                              #
x<- mtcars$mpg
xfit <- seq(min(x),max(x),length=40)          #
yfit <- dnorm(xfit,mean = mean(x),sd=sd(x))   #
yfit <- yfit*diff(h$mids[1:2]*length(x))      #
lines(xfit,yfit,col="blue",lwd=2)             #正态曲线


#核密度图
par(mfrow=c(2,1))
d <- density(mtcars$mpg)
plot(d)
k<- density(mtcars$mpg)
plot(k,main = "kernel Density of MPG")
polygon(k,col="green",border = "blue")
rug(mtcars$mpg,col="brown")

#可比较的核密度图
par(lwd=2)
library(sm)
attach(mtcars)
cyl.f <- factor(cyl,levels = c(4,6,8),
                labels = c("4 cylinder","6 cylinder","8 cylinder"))
sm.density.compare(mpg,cyl,xlab="Miles Per Gallon")
title(main="MPG distribution by Car Cylinders")

colfill <- c(2:(1+length(levels(cyl.f))))
legend(locator(1),levels(cyl.f),fill = colfill)
detach(mtcars)






































