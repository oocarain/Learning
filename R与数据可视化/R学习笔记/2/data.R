patientID <- c(1,2,3,4)
age <- c(25,34,28,52)
diabetes <- c('Type1','Type2','Type1','Type1')
status <- c('poor','improved','excellent','poor')
status <- factor(status,ordered = TRUE,levels =c ("poor","improved","excellent"))
patientdata <- data.frame(patientID,age,diabetes,status)
patientdata
str(patientdata)