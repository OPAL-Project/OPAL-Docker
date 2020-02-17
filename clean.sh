#!/usr/bin/env bash

cd Docker

docker-compose down

echo -e "All instances have been deleted.\nTo retrieve the latest images please run 'bash build.sh' otherwise please run 'bash start.sh'\n"
