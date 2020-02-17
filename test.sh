#!/usr/bin/env bash

cd test

# We pull the latest images
docker-compose pull

# We start the OPAL environment in detached mode
docker-compose up -d

cd ..

# We install the dependencies and run the end to end test
npm install && npm update
npm test

cd test

# We clean up
docker-compose down --rmi all --remove-orphans