FROM ubuntu:16.04@sha256:9775877f420d453ef790e6832d77630a49b32a92b7bedf330adf4d8669f6600e
MAINTAINER Axel Oehmichen <axelfrancois.oehmichen11@imperial.ac.uk>

WORKDIR /root

ADD insert_admin_user.py /root

RUN apt-get update -q && apt-get upgrade -y --no-install-recommends \
    && apt-get install -y python-dev python-pip \
    && pip install pymongo

CMD ["python", "insert_admin_user.py", "mongodb:27017", "admin"]
