 #2016-11-1
#第六章
#第6章 基本图形
#1简单的条形图
library(vcd)
counts <- table(Arthritis$Improved)
counts
barplot(counts,main = "Simple Bar Plot",xlab = "Improvement",ylab = "Frequency")
barplot(counts,main = "Simple Bar Plot",xlab = "Improvement",ylab = "Frequency",horiz = TRUE)

matricot <- table(Arthritis$Improved,Arthritis$Treatment)
matricot

barplot(matricot,main = "Stack plot",xlab = "Treatment",ylab = "Frequency",
        col = c("green","blue","yellow"),legend=row.names(matricot),
        args.legend =  list(title = "Improvement", x = "topright", cex = .7)) #这一句用来调整图例的大小，位置，和图例标题的

barplot(matricot,main = "Grouped Bar Plot",xlab = "Treatment",ylab = "Frequency",
        col = c("green","blue","yellow"),legend=row.names(matricot),
        args.legend =  list(title = "Improvement", x = "topright", cex = .7),
        beside = TRUE)

#均值条形图
states <- data.frame(state.region,state.x77)
means <- aggregate(states$Income,by=list(state.region),FUN=mean)
barplot(means$x,names.arg = means$Group.1,col = "blue")
title("Mean Incomes ")
png("hahah.png", width = 480, height = 480)
dev.off()


#一些饼图
#饼图创建函数 pie(x,labels)


























