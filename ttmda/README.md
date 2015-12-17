
# Tools and techniques for *massive* data analysis

This is a [CINECA](http://www.cineca.it/) [course](http://www.hpc.cineca.it/content/training-2015); last course was held [in Milano, Italy]
(http://hpc-forge.cineca.it/files/CoursesDev/public/2015/Tools_Techniques_Data_Analysis/). You may read [the official page of this course](http://www.hpc.cineca.it/content/tools-and-techniques-massive-data-analysis) to subscribe for the next one.

A read-only version of our notebooks can be accessed with [nbviewer](http://nbviewer.ipython.org/github/cineca-scai/lectures/blob/massive-analysis/ttmda) free service reading the GitHub repository.

## Prerequisites

* docker 1.9+

To install docker on a unix terminal, you can:

```
# Install docker
curl -sSL https://get.docker.com/ | sh
```

For Mac and Windows user the best way to get Docker tools working,
is using their new [toolbox](https://www.docker.com/toolbox).

## How to use lectures interactively

On a terminal:

```
$ docker run -d -p 80:8888 -v spark:/data cineca/nbsparkling
```

### Access the web jupyter notebooks pages

Visit with your browser the jupyter running server at:

[http://localhost](http://localhost).

<small>Note: if you use docker on Mac or Windows, instead of *localhost* you
should find the virtual machine IP where Docker is running.
This is usually possible with commands like `boot2docker ip` or `docker-machine ip`.</small>
