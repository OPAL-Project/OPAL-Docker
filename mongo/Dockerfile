FROM ubuntu:20.04@sha256:adf73ca014822ad8237623d388cedf4d5346aa72c270c5acc01431cc93e18e2d
MAINTAINER Axel Oehmichen <axelfrancois.oehmichen11@imperial.ac.uk>

WORKDIR /root

ADD insert_admin_user.py /root

RUN apt-get update -q && apt-get upgrade -y --no-install-recommends \
    && apt-get install -y python-dev python-pip \
    && pip install pymongo

CMD ["python", "insert_admin_user.py", "mongodb:27017", "admin"]
