# installing main libraries
install.packages('RMySQL', repos='http://cran.us.r-project.org')
library(RCurl);library(devtools);

# normal libraries (select repository)
install.packages("gplots")
install.packages("ggplot2")
install.packages("FactoMineR")
install.packages("reshape")
install.packages("reshape2")
install.packages("affy")
install.packages("affyio")

# bioconductor libraries:
source("http://bioconductor.org/biocLite.R")
biocLite("DESeq2")
biocLite("cummeRbund")
biocLite("edgeR")
biocLite("DiffBind")
