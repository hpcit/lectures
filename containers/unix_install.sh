#!/bin/bash

##################################
# CONF
project='lectures'
company='cineca-scai'
git_url="https://github.com/$company/$project.git"
branch="massive-analysis"
dir="$HOME/$project"

##################################
echo "Checking pre-requisites"

# GIT
out=`git --version 2>&1`
if [ $? -ne 0 ]; then
    echo "Missing git"
    echo "To install it, please read:"
    echo "https://git-scm.com/book/en/v1/Getting-Started-Installing-Git"
    exit 1
else
    echo "Found: $out"
fi

# Docker
out=`docker --version 2>&1`
if [ $? -ne 0 ]; then
    echo "Missing docker"
    echo "To install it, please read:"
    echo "https://docs.docker.com/installation/"
    exit 1
else
    echo "Found: $out"
fi

# Docker Compose
out=`docker-compose --version 2>&1`
if [ $? -ne 0 ]; then
    echo "Missing docker compose"
    echo "If you have python and 'pip' packager, you can:"
    echo "$ pip install docker-compose"
    echo "Otherwise read here:"
    echo "https://docs.docker.com/compose/install/"
    exit 1
else
    echo "Found: $out"
fi

##################################
# Cloning
echo -e "Good to go. Let's install! Target directory:\n$dir\n"
sleep 1

if [ -d "$dir" ]; then
    echo "[skipping clone] Project (or directory) already exists"
else
    git clone $git_url $dir
fi

##################################
# Using the massive branch
cd $dir
git checkout $branch

##################################
# Downloading images
echo "Downloading images"
sleep 1
docker-compose -f containers/massive.yml pull
