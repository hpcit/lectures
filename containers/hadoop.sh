# A hadoop/jupyter container
docker run -it -h ipyhadoop \
    -v $(pwd)/ttmda/hadoop:/data \
    -v $(pwd)/ipython_extensions:/root/.ipython/extensions:ro \
    -v $(pwd)/data:/data/worker \
    -p 80:8888 -p 8042:8042 -p 8088:8088 -p 19888:19888 \
    cineca/hadoopnotebook
