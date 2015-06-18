
# Docker image with ipython notebook server for data scientists

## Download

Get slides from github repository

```
$ git clone -b docker https://github.com/cineca-scai/lectures.git
```

## Build

This is needed only as a teacher/developer.
For students: skip to the next section.

```
$ cd lectures/docker/notebook
$ docker build -t cineca/jupydatanb .
```

## Run

If the image is not available on your host,
the first time you execute a 'run' the image will be pulled from
the official docker hub:
(linked to https://registry.hub.docker.com/u/cineca/jupydatanb)

```
# No persistent data
$ docker run -d -p 80:8000 cineca/jupydatanb

# OR using lectures (RECOMMENDED)
$ docker run -d -v $(pwd)/lectures/pydata:/data -p 80:8000 cineca/jupydatanb
```

Then open with your browser: [http://localhost](http://localhost) and *enjoy*!

## Use the image with both Python2 and R kernels

The normal image is ~ 1.5 GB.
The one with additional R core is ~ 2.5 GB.

To run the most complete one:
```
$ docker run -d -v /your/path/to/nbs/files:/data -p 80:8000 cineca/jupydatar
```
