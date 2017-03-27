#############################################################################
######## function that randomly generates the bivariate example data #########
##############################################################################
genData=function(nrow=nrow,sd=sd,real.centers=real.centers,seed=seed){
  set.seed(seed) 
  data <- matrix(nrow=0, ncol=2)
  colnames(data) <- c("x", "y")
  labels=numeric() # this vector stores the actual classification of the data
  
  #randomly generated bivariate data (using rnorm)
  for (i in 1:length(real.centers$x)) {
    x0 <- rnorm(nrow, mean=real.centers$x[[i]], sd=sd[i])
    y0 <- rnorm(nrow, mean=real.centers$y[[i]], sd=sd[i])
    labels=c(labels,rep(i,times=nrow))
    data <- rbind( data, cbind(x0,y0) )
  }
  return(list(data=data,labels=labels))
}
