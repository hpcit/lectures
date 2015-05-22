
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
# No persistent data
$ docker run -d -p 80:80 cineca/jupydatanb

# OR using lectures (work in progress)
$ docker run -d -v $(pwd)/lectures/pydata:/home/pydatanalysis/nbs -p 80:80 cineca/jupydatanb
```

Then open with your browser: [http://localhost](http://localhost)

username: pydatanalysis
password: workshop
