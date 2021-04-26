FROM ubuntu:16.04@sha256:eed7e1076bbc1f342c4474c718e5438af4784f59a4e88ad687dbb98483b59ee4
MAINTAINER Shubham Jain <s.jain@imperial.ac.uk>

WORKDIR /root

RUN apt-get update -q && apt-get upgrade -y --no-install-recommends \
    && apt-get install -y git \
    && apt-get install -y postgresql-client

RUN git clone https://github.com/OPAL-Project/OPAL-Database.git

CMD sleep 2 ; psql -h timescaledb -U postgres -tc "SELECT 1 FROM pg_database WHERE datname = 'opal'" | grep -q 1 || psql -h timescaledb -U postgres -c "CREATE DATABASE opal" ; psql -h timescaledb opal postgres -f OPAL-Database/timescaledb/timescale.sql
