mydata <- data.frame(dose=numeric(0),
                     drugA=numeric(0),
                     drugB=numeric(0))
fix(mydata)
dose <- mydata$dose
drugA <- mydata$drugA
drugB <- mydata$drugB
opar <- par(no.readonly = TRUE)
par(pin = c(2,3))
par(lwd=2,cex=1.5)
par(cex.axis=.75,font.axis=3)
plot(dose,drugA,type = "b",pch =19,lty=2,col="red")
plot(dose,drugB,type = "b",pch =23,lty=6,col="blue",bg="green")
par(opar)

#下面是p50代码
par(ann=FALSE)
plot(dose,drugA,type = "b",
     col="red",lty=2,pch=2,lwd=2,
     xlim =c(0,60),ylim=c(0,70))
title(main="clinical Trials for DrugsA",col.main="red",
      sub="This is hypothetical data",col.sub="blue",
      xlab = "Dosage",ylab = "Drug Response",
      col.lab="green",cex.lab=0.75)
#代码清单3-2 P32 自定义坐标轴的事例
x <- c(1:10)
y <- x
z <- 10/x
opar <- par(no.readonly = TRUE)

par(mar=c(5,4,4,8) + 0.1)

plot(x,y,type = "b",
     pch=21,col="red",
     yaxt="n",lty=3,ann=FALSE)

lines(x,z,type = "b",pch=22,col="blue",lty=2)

axis(2,at=x,labels=x,col.axis="red",las=2)

axis(4,at=z,labels = round(z, digits = 2),col.axis="blue",las=2,cex.axis=0.7,tck=-.01)

mtext("y=10/x",side = 4,line = 3,cex.lab=1, las=2,col="blue")

title(main="An Example of Creative Axes",xlab="x values",ylab="Y=X")

par(opar)

#代码清单3-3 p55
dose <- c(20,30,40,45,60)
drugA <- c(16,20,27,40,60)
drugB <- c(15,18,25,31,40)

opar <- par(no.readonly = TRUE)

par(lwd=2,cex=1.5,font.lab=2)

plot(dose,drugA,type = "b",
     pch =15,lty =1,col="red",ylim=c(0,60),
     main="DrugA VS DrugeB",
     xlab = "Druge Dose",ylab = "Drug Response")
     
 lines(dose,drugB,type = "b",
       pch=17,lty=2,col="blue")
 
 abline(h=c(30),lwd=1.5,lty=2,col="gray")
 
 library(Hmisc)
 minor.tick(nx=3,ny=3,tick.ratio = 0.5)
 
 legend("topleft",inset = .05,title = "Drug Type",c("A","B"),
        lty = c(1,2),pch=c(15,17),col = c("red","blue"))
par(opar)

#文本标注 p56
attach(mtcars)
plot (wt,mpg,
      main = "Mileage vs. Car Weight",
      xlab ="weight",ylab = "Mileage",
      pch=18,col="blue")
text(wt,mpg,
     row.names(mtcars),
     cex=0.6,pos=4,col="red")
detach(mtcars)

#展示不同字体族的代码
opar <- par(no.readonly = TRUE)
par(cex=1.5)
plot(1:7,1:7,type="n")
text(3,3,"example of default text")
text(4,4,family="mono","example of default text")
text(5,5,family="serif","example of default text")
text(6,6,family="sans","example of default text")
par(opar)

#图形组合 p59 图3-14
attach(mtcars)
opar <- par(no.readonly = TRUE)
par(mfrow = c(2,2))
plot(wt,mpg,main ="wt vs. mpg")
plot(wt,disp,main ="wt vs. disp")
hist(wt,main ="Histogram of wt")
boxplot(wt,main ="Boxplot of wt")
par(opar)
detach(mtcars)

#图形组合 p59 图3-15
attach(mtcars)
opar <- par(no.readonly = TRUE)
par(mfrow = c(3,1))
hist(wt)
hist(disp)
hist(mpg)
par(opar)
detach(mtcars)

#图形组合 p60 图3-16 nd 图3-17
attach(mtcars)
layout(matrix(c(1,1,2,3),2,2,byrow = TRUE),
       widths=c(3,1),heights=c(1,2))       #此句去掉为3-16的图
hist(wt)
hist(mpg)
hist(disp)
detach(mtcars)
#对上面的升级一下来验证layout如何控制图形分布
attach(mtcars)
layout(matrix(c(1,2,3,4,5,5),3,2,byrow = TRUE))
hist(wt)
hist(mpg)
hist(disp)
hist(wt)
hist(mpg)
detach(mtcars)

#代码清单3-4 p62 图形布局的精细控制
opar <- par(no.readonly = TRUE)
par(fig=c(0,0.8,0,0.8))
plot(mtcars$wt,mtcars$mpg,
     xlab = "Miles per Gallon",
     ylab="Car Weight")
par(fig=c(0,0.8,0.55,1),new=TRUE)
boxplot(mtcars$wt,horizontal = TRUE,axes = FALSE)
par(fig=c(0.65,1,0,0.8),new=TRUE)
boxplot(mtcars$mpg,axes=FALSE)
mtext("Enhanced Scatterplot",side = 3,outer = TRUE,line=-3)
par(opar)













