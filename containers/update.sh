
# Update images available

images="busybox cineca/sparkcluster cineca/sparknotebook cineca/hadoopnotebook"

for i in $images;
do
    echo "Updating $i"
    docker pull $i
done
