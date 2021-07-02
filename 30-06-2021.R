bookD <- Book1

summary(bookD)

# factor : Convert into categorycal data 
bookD$gender=as.factor(bookD$gender)

# imputation
#
bookD$gender=as.factor(bookD$gender)

library(mice)

# mice( dataset, num_of_predict, numofmethod=numofcol, num of iteration)
imp = mice(bookD,m=5, method=c("","pmm","logreg"),maxit=20)

finalDataset1= complete(imp,1)
finalDataset2= complete(imp,2)
finalDataset3= complete(imp,3)
finalDataset4= complete(imp,4)
finalDataset5= complete(imp,5)


# boxplot
dt <- BigMartSales
d <- boxplot(dt$Item_MRP,ylab="shfkjs",xlab="hfsjk")

# data spred ! IRQ outlier detaction
q1 <- quantile(dt$Item_MRP,0.25)
q2 <- quantile(dt$Item_MRP,0.50)
q3 <- quantile(dt$Item_MRP,0.75)

IQR <- q3-q1

upper <- q3+(1.5*IQR)
lower <- abs(q1-(1.5*IQR))
upper
mean(dt$Item_MRP)

# found column
outDt <- which(dt$Item_MRP< lower | dt$Item_MRP > upper)
outDt

library(data.table)
library(mltools)

onehot_data <- one_hot(as.data.table(dt),naCols = TRUE)
onehot_data
