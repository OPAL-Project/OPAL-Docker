FROM ubuntu:16.04@sha256:eed7e1076bbc1f342c4474c718e5438af4784f59a4e88ad687dbb98483b59ee4
MAINTAINER Axel Oehmichen <axelfrancois.oehmichen11@imperial.ac.uk>

WORKDIR /root

ADD insert_admin_user.py /root

RUN apt-get update -q && apt-get upgrade -y --no-install-recommends \
    && apt-get install -y python-dev python-pip \
    && pip install pymongo

CMD ["python", "insert_admin_user.py", "mongodb:27017", "admin"]
