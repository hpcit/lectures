#!/bin/bash

echo "Pull updates"
cd /data/lectures
git checkout $LECTURE_BRANCH && git pull origin $LECTURE_BRANCH
echo "Updated"
#ls /data/lectures/*/*ipynb
chown -R $NB_USER /data 2> /dev/null
echo "Permission fixed"

