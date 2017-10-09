#!/bin/bash  

#####  APP specific variables  #######
DOCKER_USER=macxxn
IMAGE_NAME=auto_tutorial
IMAGE_TAG=latest

CONTAINER_NAME=auto_tutorial
CONTAINER_PORT=9528
HOST_BIND_PORT=9528
######################################

echo "running containers:"
docker ps
echo ""

echo "stop and remove existing container below:"
docker rm -f ${CONTAINER_NAME}

echo ""
echo "port mapping:"
echo "host:container = "${HOST_BIND_PORT}":"${CONTAINER_PORT}
echo ""

docker run -p ${HOST_BIND_PORT}:${CONTAINER_PORT} -d --name ${CONTAINER_NAME} -t ${DOCKER_USER}/${IMAGE_NAME}':'${IMAGE_TAG}

echo ""
echo "service available at:"
echo "http://localhost:${HOST_BIND_PORT}"