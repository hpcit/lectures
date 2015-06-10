#/bin/bash
docker run -d -v $(pwd)/lectures/pydata:/data -v /tmp/statistics/:/statistics -p 80:8000 cineca/jupydatanb
