
# A hadoop/jupyter container
docker run -d -h ipyhadoop \
    --name containers_hadoopclient_1 \
    -v $(pwd)/ttmda/hadoop:/data \
    -v $(pwd)/ipython_extensions:/root/.ipython/extensions:ro \
    -v $(pwd)/data:/data/worker \
    -p 80:8888 -p 8042:8042 -p 8088:8088 -p 19888:19888 \
    cineca/hadoopnotebook

docker logs -f containers_hadoopclient_1

exit;

# To clean:
containers="containers_hadoopclient_1"
docker stop $containers
docker rm -v $containers
