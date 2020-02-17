#!/usr/bin/env bash

cp ./Docker/daemon.json /etc/docker/daemon.json
service docker restart
rm -rf Docker/*.config.js

echo -e "Copying all config files to Docker folder for docker-compose\n"

for file in config/*.sample.config.js; do
    newName=`echo $file | sed s/sample.config.js/config.js/ | sed s/config/Docker/`
    cp $file  $newName
done

echo "Setting up server $1"

# create /mnt/db/pgdata for timescaledb data
# create /mnt/db/mongodata for mongodb data for server 1

cd Docker

echo -e "Building the images\n"

docker-compose -f docker-compose-server-$1.yml build

echo -e "\nPulling the latest Docker images from DockerHub\n"

docker-compose  -f docker-compose-server-$1.yml pull

echo -e "\nPlease check the configuration files then start the OPAL Platform with 'bash start.sh'\n"
