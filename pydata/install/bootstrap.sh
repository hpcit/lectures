#!/bin/bash

# Go to your home directory and remove existing project
cd $HOME
rm -rf lectures
# Clone this repo
echo "Clone git repo"
git clone --branch=milano https://github.com/cineca-scai/lectures.git
# Removing existing
nohup sudo docker rm -f $(docker ps -aq -f name=notebook) 2> /dev/null
# Launch the ipython jupyter server: a new container
echo "Launch a new conainer"
sudo docker run -d -p 80:8000 -v $HOME/lectures/pydata:/data --name notebook cineca/jupydatanb