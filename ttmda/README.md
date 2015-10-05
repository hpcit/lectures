
# Tools and techniques for *massive* data analysis

This is a [CINECA](http://www.cineca.it/) [course](http://www.hpc.cineca.it/content/training-2015).

You can read [the official page of this course](http://www.hpc.cineca.it/content/tools-and-techniques-massive-data-analysis).

Other material is also available [here](https://hpc-forge.cineca.it/files/CoursesDev/public/2015/Tools_Techniques_Data_Analysis/).

A read-only notebooks version can be viewed with [nbviewer](http://nbviewer.ipython.org/github/cineca-scai/lectures/blob/massive-analysis/ttmda) free service.

## Prerequisites

* git 1.7+
* docker 1.8+
* docker-compose 1.4+

To install docker and docker-compose on a unix terminal, you can:

```
# Install docker
curl -sSL https://get.docker.com/ | sh

# Install docker-compose
pip install -U docker-compose
```

For Mac and Windows user the best way to get Docker tools working,
is using their new [toolbox](https://www.docker.com/toolbox).

## How to use lectures interactively

Clone the repo and use docker compose configuration.
On a terminal:

```
# Download this repository
$ git clone https://github.com/cineca-scai/lectures.git

# Use the branch for this specific lecture
$ cd lectures && git checkout massive-analysis

# Download docker images (warning: size ~ 5GB)
$ docker-compose -f containers/spark.yml pull

# Bring up the Spark cluster and the Jupyter notebook server
$ docker-compose -f containers/spark.yml up
```

Then visit with your browser the jupyter running server at:

[http://localhost](http://localhost).

<small>Note: if you use docker on Mac or Windows, instead of *localhost* you
should find the virtual machine IP where Docker is running.
This is usually possible with commands like `boot2docker ip` or `docker-machine ip`.</small>

## How to test only the notebook server

```
docker-compose -f containers/spark.yml up --no-deps client
```
