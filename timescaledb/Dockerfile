FROM ubuntu:16.04@sha256:0d06090fff94c0a3640729c7ef7e6b36ad5b41bec600cc2be92739c90d204243
MAINTAINER Shubham Jain <s.jain@imperial.ac.uk>

WORKDIR /root

RUN apt-get update -q && apt-get upgrade -y --no-install-recommends \
    && apt-get install -y git \
    && apt-get install -y postgresql-client

RUN git clone https://github.com/OPAL-Project/OPAL-Database.git

CMD sleep 2 ; psql -h timescaledb -U postgres -tc "SELECT 1 FROM pg_database WHERE datname = 'opal'" | grep -q 1 || psql -h timescaledb -U postgres -c "CREATE DATABASE opal" ; psql -h timescaledb opal postgres -f OPAL-Database/timescaledb/timescale.sql
