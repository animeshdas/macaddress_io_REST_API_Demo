# set the base image

FROM python:2.7

# author

MAINTAINER Animesh Das <jobs4ani@gmail.com>

LABEL version="0.1"

LABEL description="First image with Dockerfile."

RUN mkdir -p /Demo

ADD check_mac.py /Demo/.

ADD macaddress_io.apikey /Demo/.

#RUN pip install requests

RUN if [ $(pip list | grep requests) ]; then echo "Python package already installed"; else echo "Python packages not installed. Installing...."; pip install requests; fi