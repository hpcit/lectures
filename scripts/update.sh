#!/bin/bash

echo "Pull updates"
cd /data/lectures
git checkout science-rome
git pull origin science-rome
echo "Updated:"
ls /data/lectures/*ipynb

