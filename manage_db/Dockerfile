FROM python:latest
USER root
RUN apt-get update &&\
    apt-get install build-essential libssl-dev libffi-dev python3-dev python3-pip curl -y &&\
    curl -LJo /mnt/nginx_logs.txt https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs &&\
    pip3 install psycopg2 python-dateutil
    