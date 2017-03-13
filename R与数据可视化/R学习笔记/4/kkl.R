library(xlsx)
jkl <- "c:/Users/Administrator/Desktop/oppo.xlsx"
mydata <- read.xlsx(jkl,1)
names(mydata)
dim(mydata)
head(mydata)
tail(mydata)
ls()
