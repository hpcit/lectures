
# Docker image with ipython notebook server for data scientists

## Download

```
$ git clone -b docker https://github.com/cineca-scai/lectures.git
```

## Build

```
$ cd lectures/docker/notebook
$ docker build -t cineca/jupydatanb .
```

## Run

```
$ docker run -d -v $(pwd)/lectures/pydata:/home/pydatanalysis/nbs -p 80:80 cineca/jupydatanb
```