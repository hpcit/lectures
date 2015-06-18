
# Docker image with ipython notebook server for data scientists

## Ipython2 kernel + R kernel

To run the notebook server on your machine:
```
$ docker run -d -v /your/path/to/nbs/files:/data -p 80:8000 cineca/jupydatar
```

Then open with your browser: [http://localhost](http://localhost) and *enjoy*!
