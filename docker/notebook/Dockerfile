
FROM jupyter/jupyterhub
MAINTAINER Paolo D. <p.donoriodemeo@cinecait>

# reference:
# first part inspired on
# https://registry.hub.docker.com/u/twiecki/pydata-docker-jupyterhub

ENV PYVERSION 2
ENV PYDATAPKG six numpy scipy pandas matplotlib seaborn scikit-learn statsmodels

##########################
# APT
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y \
        wget libsm6 libxrender1 libfontconfig1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
##########################
# CONDA
RUN wget --quiet \
    https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh && \
    bash Miniconda-latest-Linux-x86_64.sh -b -p /opt/miniconda && \
    rm Miniconda-latest-Linux-x86_64.sh
ENV PATH /opt/miniconda/bin:$PATH
RUN chmod -R a+rx /opt/miniconda