
# A spark cluster with master and worker. Also a jupyter notebook as a client.

#master
docker run -d \
    -h master --name containers_master_1 \
    -e SPARK_MASTER_HOST=master \
    --expose=7077 -p 8080:8080 \
    cineca/sparkcluster /bootmaster.sh

#worker
docker run -d \
    -h worker --name containers_worker_1 \
    -e SPARK_MASTER_HOST=master \
    -e SPARK_WORKER_WEBUI_PORT=8081 \
    -e SPARK_WORKER_CORES=2 -e SPARK_WORKER_MEMORY=1g \
    -p 8081:8081 --link containers_master_1:master \
    -v $(pwd)/data:/data/worker \
    cineca/sparkcluster /bootslave.sh

#client
docker run -d \
    -h worker --name containers_sparkclient_1 \
    -e MASTER=spark://master:7077 \
    -link containers_master_1:master -link containers_worker_1:worker \
    -p 80:8888 \
    -v $(pwd)/ttmda/spark:/data \
    -v $(pwd)/data:/data/worker \
    cineca/sparknotebook

docker logs -f containers_sparkclient_1

exit;

# To clean:
containers="containers_master_1 containers_worker_1 containers_sparkclient_1"
docker stop $containers
docker rm -v $containers
