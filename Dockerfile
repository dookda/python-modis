FROM ubuntu

# http://www.pymodis.org/ docker image

MAINTAINER Luca Delucchi

# system environment
ENV DEBIAN_FRONTEND noninteractive
#### ENV CPLUS_INCLUDE_PATH=/usr/include/gdal \
####    C_INCLUDE_PATH=/usr/include/gdal

# ??     && apt-get install -y --install-recommends \

# fetch dependencies
RUN apt update && DEBIAN_FRONTEND="noninteractive" TZ="Asia/Bangkok" apt-get install -y tzdata
RUN apt update && apt install -y software-properties-common
RUN apt update && add-apt-repository ppa:ubuntugis/ppa
RUN apt-get update \
    && apt-get install -y \
    gdal-bin \
    python3-numpy \
    python3 \
    python3-gdal \
    ipython3 \
    python3-pip \
    python3-future \
    python3-requests
RUN apt-get update  & apt install python3-pip
RUN install -y gdal-bin libgdal-dev
#    && apt-get autoremove \
#    && apt-get clean

# Install pyModis
#####? RUN pip install GDAL==$(gdal-config --version | awk -F'[.]' '{print $1"."$2}')
RUN pip3 install pyModis
RUN pip3 install pygdal=="`gdal-config --version`.*"
RUN pip3 install geoserver-rest