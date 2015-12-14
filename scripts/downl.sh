#!/bin/bash
dir="/data/lectures/ttmda/hadoop/tmp"
myfile="$dir/ngs.sam"

# Create directory
mkdir -p $dir
rm -f $myfile
echo "Path ready"

# Download compressed NGS data from a link
wget "http://bit.ly/ngs_sample_data" -O $myfile.bz2
echo "Downloaded"

# Decompress the file
bunzip2 $myfile.bz2
echo "Decompressed"

# Running as root...
echo ". /data/lectures/scripts/hadoop_env.sh" >> /home/$NB_USER/.bashrc
chown -R $NB_USER /data
#hadoop fs -chown -R $NB_USER /
echo "Fixed permissions"

# cd /tmp \
#     && git clone https://github.com/Yelp/mrjob \
#     && cd mrjob && pip install -e .
