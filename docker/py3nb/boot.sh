#!/bin/bash

dir="/data"
project="lectures"
branch="science-rome"
nbpath="pyscience"

cd $dir

if [ -d $project ]; then
    echo "Repository already found"
else
    git clone https://github.com/cineca-scai/lectures.git
fi

cd $project
git checkout $branch
git pull origin $branch
chown -R $NB_UID /data
echo "Done repository init"

cd $nbpath
start-notebook.sh
