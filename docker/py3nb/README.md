
# Docker image for Jupyter Notebook

## What it contains

* Working notebook Python3 environment
* Based on Jupyter docker stacks
* Installed on latest ubuntu
* Use of latest Conda package repository
* Using Python 3.5
* Adding Live slideshow and Mathj offline
* Pulling the latest Github Lectures and boot from there

## How to run

```bash
docker run -it -v science:/data -p 80:8888 cineca/nbscience
```