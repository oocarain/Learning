#第七次实验--植物激素提取，纯化，测量
#下面是制作标准曲线

c_of_sample <- c(10,5,2.5,1.25,0.625,0.3125) #样品1-7的浓度
avg_of_sample_OD <- c(0.5377,0.6585667,0.7382667,0.8450333,
                      0.9266333,1.0364667)
log_of_c <- log10(c_of_sample) # 以此为横坐标 
Bi <- avg_of_sample_OD                                                 #样品1-7，每个样品做三次重复得到平均的OD值log_of_c <-log10(c_of_sample)      #对浓度取log  
Bo <- 1.2412666               #样品中不含IAA时测的的OD值
ln_of_OD <- log(Bi/(Bo-Bi))   #以此为纵坐标

mydata <- data.frame(log_of_c,ln_of_OD)
mydata
fit <- lm(log_of_c ~ ln_of_OD,data = mydata)
opar <- par(no.readonly = TRUE)
con <- seq(-0.6,1,0.25)
OD <- seq(1.8,-0.8,-0.35)
plot(mydata$log_of_c,mydata$ln_of_OD,
     xaxt="n",yaxt="n",ann = FALSE
)
axis(1,at=con,lables="log[IAA]",las=0)
axis(2,at=OD,lables="ln[Bi/(Bo/Bi)]",las=0)
abline(fit)
title(main="浓度-吸光度标准曲线",xlab= "log[IAA]",
      ylab ="ln[Bi/(Bo/Bi)]")
par(opar)

