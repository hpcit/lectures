#!/bin/bash

branch='massive-analysis'
echo "Pull updates"
cd /data/lectures
git checkout $branch && git pull origin $branch
echo "Updated"
#ls /data/lectures/*/*ipynb
chown -R $NB_USER /data
echo "Permission fixed"

