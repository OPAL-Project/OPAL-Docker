#!/usr/bin/env bash

echo -e 'Hang tight, the OPAL platform is about to start.'

cd Docker

docker-compose -f docker-compose-server-1.yml -f docker-compose-server-2.yml up
