library(ggplot2)
library(ggmap)
library(XML)
library(maps)
library(mapproj)
url <- 'http://data.earthquake.cn/datashare/globeEarthquake_csn.html' 
tables <- readHTMLTable(url,stringAsFactors=FALSE,encoding="UTF-8")
raw <- tables[[6]]
data <- raw[,c(1,3,4)]
names(data) <- c('date','lan','lon')
data$lan <- as.numeric(data$lan)
data$lon <- as.numeric(data$lon)
data$date <- as.Date(data$date,"%Y-%m-%d")
ggmap(get_googlemap(center = 'china',zoom = 4,maptype = 'terrain'),extent = 'device')+geom_point(data=data,aes(x=lon,y=lan),colour='red',alpha=0.4)+
opts(lengend.position="none")
