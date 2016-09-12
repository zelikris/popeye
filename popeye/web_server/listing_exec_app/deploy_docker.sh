#!/bin/bash

# remove all docker containers
docker rm $(docker ps -a -q)

if [ -z "$(docker images | grep anaconda-lib)" ];
then
    echo "image does not exist, building..."
    docker build -t anaconda-lib .
    echo "done, test"
    docker images
else
    echo "image exists"
fi
