FROM ubuntu:16.04@sha256:a3785f78ab8547ae2710c89e627783cfa7ee7824d3468cae6835c9f4eae23ff7
MAINTAINER Shubham Jain <s.jain@imperial.ac.uk>

WORKDIR /root

RUN apt-get update -q && apt-get upgrade -y --no-install-recommends \
    && apt-get install -y git \
    && apt-get install -y postgresql-client

RUN git clone https://github.com/OPAL-Project/OPAL-Database.git

CMD sleep 2 ; psql -h timescaledb -U postgres -tc "SELECT 1 FROM pg_database WHERE datname = 'opal'" | grep -q 1 || psql -h timescaledb -U postgres -c "CREATE DATABASE opal" ; psql -h timescaledb opal postgres -f OPAL-Database/timescaledb/timescale.sql
