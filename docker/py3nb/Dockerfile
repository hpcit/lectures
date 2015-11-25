# Python3 Notebook for data scientists and CINECA courses

FROM ubuntu:15.10
MAINTAINER "Paolo D'Onorio De Meo <p.donoriodemeo@gmail.com>"

######################
# Install all OS dependencies for fully functional notebook server
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -yq --no-install-recommends \
    git vim wget build-essential python-dev bzip2 unzip libsm6 \
    ca-certificates pandoc sudo \
    libglib2.0-0 libxext6 libxrender1 libxml2-dev libxslt1-dev \
    # texlive-latex-base texlive-latex-extra \
    # texlive-fonts-extra texlive-fonts-recommended \
    && apt-get clean && rm -rf /tmp/*

######################
# Install Tini
RUN wget --quiet https://github.com/krallin/tini/releases/download/v0.6.0/tini && \
    echo "d5ed732199c36a1189320e6c4859f0169e950692f451c03e7854243b95f4234b *tini" | sha256sum -c - && \
    mv tini /usr/local/bin/tini && \
    chmod +x /usr/local/bin/tini

######################
# Configure environment
ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH
ENV CONDA_REPO https://repo.continuum.io/miniconda
ENV CONDA_BIN Miniconda3-latest-Linux-x86_64.sh
ENV CONDA_URL $CONDA_REPO/$CONDA_BIN
ENV SHELL /bin/bash
ENV NB_USER jovyan
ENV NB_UID 1000

######################
# Install conda
RUN mkdir -p $CONDA_DIR && \
    echo export PATH=$CONDA_DIR/bin:'$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet $CONDA_URL && \
    /bin/bash /$CONDA_BIN -f -b -p $CONDA_DIR && rm $CONDA_BIN && \
    $CONDA_DIR/bin/conda install --yes conda==3.18.6 && \
    conda clean --tarballs
    # && conda clean --source-cache

######################
# Install Jupyter notebook
RUN conda install --yes \
    'notebook=4.*' terminado \
    && conda clean -yt

######################
# Create jovyan user with UID=1000 and in the 'users' group
# Grant ownership over the conda dir and home dir, but stick the group as root.
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
    mkdir /home/$NB_USER/work && \
    mkdir /home/$NB_USER/.jupyter && \
    mkdir /home/$NB_USER/.local && \
    chown -R $NB_USER:users $CONDA_DIR && \
    chown -R $NB_USER:users /home/$NB_USER

######################
# Configure container startup
EXPOSE 8888
ENTRYPOINT ["tini", "--"]
CMD ["start-notebook.sh"]

######################
# Add startup scripts from github
# https://github.com/jupyter/docker-stacks/tree/master/minimal-notebook
ENV JUPY_GITHUB https://raw.githubusercontent.com/jupyter/docker-stacks/master

ENV SCRIPT start-notebook.sh
ENV JUPY_STARTSCRIPT $JUPY_GITHUB/minimal-notebook/$SCRIPT
RUN wget $JUPY_STARTSCRIPT -q -O /usr/local/bin/$SCRIPT && \
    chmod +x /usr/local/bin/$SCRIPT

ENV JUPY_CONFIG $JUPY_GITHUB/minimal-notebook/jupyter_notebook_config.py
RUN wget $JUPY_CONFIG -q -O /home/$NB_USER/.jupyter/jupyter_notebook_config.py
RUN chown -R $NB_USER:users /home/$NB_USER/.jupyter
RUN rm -rf /tmp/*

######################
USER jovyan
# Install Python 3 packages
RUN conda install --yes ipywidgets \
    pandas matplotlib scipy seaborn bokeh \
    scikit-learn scikit-image sympy cython \
    patsy statsmodels cloudpickle dill numba \
    && conda clean -yt

#####################
# Live slideshows
WORKDIR /tmp
RUN wget -q https://github.com/pdonorio/RISE/archive/master.tar.gz \
    && tar xvzf *.gz && cd *master && \
    python setup.py install > /tmp/rise.log && rm -rf /tmp/*

#####################
# Cineca lectures
ADD boot.sh /boot.sh

######################
WORKDIR /data
USER root
RUN chmod +x /boot.sh
ENV TERM xterm
CMD ["/boot.sh"]

## docker run -it -v science:/data -p 80:8888 cineca/nbscience


# # WORKAROUND: symlink version of zmq required by latest rzmq back into conda lib
# # https://github.com/jupyter/docker-stacks/issues/55
# RUN ln -s /opt/conda/pkgs/zeromq-4.0.*/lib/libzmq.so.4.* /opt/conda/lib/libzmq.so.4
# RUN ln -s /opt/conda/pkgs/libsodium-0.4.*/lib/libsodium.so.4.* /opt/conda/lib/libsodium.so.4