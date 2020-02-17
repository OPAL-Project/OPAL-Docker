# OPAL-Docker

This repository contains deployment information, deployment scripts (docker-compose) and a testing script to test the deployment of the OPAL platform.

Please not that the **_OPAL platform officially supports only Ubuntu 16.06 LTS and node 8.x or above_**. Other Linux like environments are compatible (debian, macOS, etc.) but are not officially supported. 

## How to build images locally

```sh
# build
sudo docker build -f DockerHub/Dockerfile -t opalservices/opal-<servicename>:latest .

# push
sudo docker push opalservices:opal-<servicename>:latest
```

## Sandbox environment

You can test locally a small deployment of the OPAL platform (1 Interface, 1 Cache, 1 Algorithm Service, 1 Scheduler, 1 Compute , 1 Database and 1 Privacy) using [docker-compose](https://docs.docker.com/compose/).
to facilitate the process three bash scripts have been developed: 
  * `build.sh` : Copies the sample config to the Docker folder and pulls the latest version of all the necessary Docker images from DockerHub.
  * `start.sh` : Starts the cluster.
  * `clean.sh` : Removes all containers used by the OPAL compose. **NB**: The other containers and the OPAL container images will not be deleted. 
  * `test.sh` : Runs a small end to end test against the sandbox environment to check if the OPAL running from docker-compose runs properly.

Please be aware that the interface will start on port `80`, the database on port `5432` and mongo on `27017`. Thus, before starting the sandbox please make sure that those three ports are available.
