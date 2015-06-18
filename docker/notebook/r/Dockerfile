
FROM cineca/jupydatanb
MAINTAINER Paolo D. <p.donoriodemeo@cineca.it>

##########################
# Ubuntu distro R core
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" \
    >> /etc/apt/sources.list && \
    gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 \
    && gpg -a --export E084DAB9 | sudo apt-key add - \
    && apt-get update && apt-get upgrade -y && apt-get install -y \
    r-base r-base-dev \
    libssl-dev libxml2-dev libcurl4-openssl-dev libzmqpp-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

##########################
# Define CRAN mirror
RUN echo "local({r <- getOption('repos'); r['CRAN'] <- 'http://cran.r-project.org'; options(repos=r)});" >> /root/.Rprofile

##########################
# Development tools
ADD kernel_packages.r /tmp/script1.r
RUN R --no-save < /tmp/script1.r
# Data packages
ADD data_analysis_packages.r /tmp/script2.r
RUN R --no-save < /tmp/script2.r

##########################
# Install notebook kernel
#USER $myuser
ENV rscript /tmp/Rscripting.Ruser
RUN ipython kernelspec install --replace --name ir --user \
    /usr/local/lib/R/site-library/IRkernel/kernelspec && \
    echo "library(IRdisplay); library(IRkernel); installspec()" > $rscript \
    && R --no-save < $rscript

#########################
#Clean
RUN rm -fr /tmp/*
