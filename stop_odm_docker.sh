#! /bin/sh
container_id=$(docker ps -a -q --filter="name=hkuuas-mapping")
docker container stop $container_id && docker container rm $container_id