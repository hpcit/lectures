# Tools and techniques for massive data analysis

This is a [CINECA](http://www.cineca.it/) [course](http://www.hpc.cineca.it/content/training-2015).

Latest material is available [here](https://hpc-forge.cineca.it/files/CoursesDev/public/2015/Tools_Techniques_Data_Analysis/).

A read-only notebooks version can be viewed with [nbviewer](http://nbviewer.ipython.org/github/cineca-scai/lectures/blob/massive-analysis/ttmda/Mrjob.ipynb) free project.

## Prerequisites

Install git.

Also install docker and docker-compose. For example:

```
# Install docker
curl -sSL https://get.docker.com/ | sh
# Install docker-compose
pip install -U docker-compose
```

## How to use lectures interactively

```
$ git clone https://github.com/cineca-scai/lectures.git
$ cd lectures && git checkout massive-analysis
$ docker run -it -v $(pwd)/ttmda:/data -p 80:8888 pdonorio/py3mapreduce /opt/start
```

Then visit with your browser the jupyter running server at:

[http://localhost](http://localhost).

<small>Note: if you use docker on Mac or Windows, instead of localhost you
should find the virtual machine IP. E.g. `boot2docker ip`.</small>
