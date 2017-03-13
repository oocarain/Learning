your.name <- c("oocarain","javen","lantian")
your.score <- c(8,9,7)
your.ID <- c("20161011","20161013","20161014")
mydata <- data.frame(your.ID,your.name,your.score)
mydata
ST1 <- data.frame(your.ID,your.name)
ST2 <- data.frame(your.ID,your.score)
ST1
ST2
TO_ST <- merge(ST1,ST2,by ="your.ID")
TO_ST