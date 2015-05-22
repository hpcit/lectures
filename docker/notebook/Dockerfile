
FROM jupyter/jupyterhub
MAINTAINER Paolo D. <p.donoriodemeo@cinecait>

## PYTHON 2 ORIENTED
# Inspired by:
## https://registry.hub.docker.com/u/twiecki/pydata-docker-jupyterhub
# And also from:
## https://github.com/rothnic/anaconda-notebook

ENV PYVERSION 2
ENV PYDATAPKG six numpy scipy pandas matplotlib seaborn bokeh scikit-learn

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
##########################
# Install PyData modules and IPython dependencies
RUN conda update --quiet --yes conda && \
    conda install --quiet --yes $PYDATAPKG \
        pip sqlalchemy cython pyzmq statsmodels \
        theano tornado jinja2 sphinx pygments nose readline \
    && conda clean -y -t
##########################
# Update kernels
WORKDIR /srv/ipykernel
RUN pip install pip -U \
    && rm -rf /usr/local/share/jupyter/kernels/* \
    && pip2 install -r requirements.txt -e .
RUN ipython kernelspec install-self
##########################
# SLIDES & pdf
RUN pip2 install jsonschema mistune
# # PDF generation ?
# RUN apt-get update && apt-get install -y \
#     texlive-latex-base texlive-latex-recommended texlive-fonts-recommended \
#     texlive-fonts-extra texlive-latex-extra \
#     && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
##########################
# ADD jupyterhub USER
ENV myuser pydatanalysis
ENV mypw workshop
ADD add_user.sh /tmp/add.sh
RUN echo "$myuser,$mypw" > /tmp/users && bash /tmp/add.sh /tmp/users
USER $myuser
##########################
# MATHJAX
# Install MathJax locally because it has some problems with https
#as reported here: https://github.com/bgruening/galaxy-ipython/pull/8
RUN python2 -c \
    'from IPython.external import mathjax; mathjax.install_mathjax("2.5.1")'
RUN ipython profile create
##########################
# LIVE RELOAD MY SLIDES?
WORKDIR /tmp
# Does not work...
RUN git clone https://github.com/damianavila/RISE.git
RUN cd RISE && python2 setup.py install

# ##########################
# # Change keys and profiles
# USER root
# ADD main.js /home/$myuser/.ipython/nbextensions/livereveal/main.js
# RUN chown $myuser -R /home/$myuser/.ipython

# ##########################
# # Clean
# RUN rm -fr /tmp/*
