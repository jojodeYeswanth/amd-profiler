FROM ubuntu:20.04
COPY . .
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install -e .

CMD ["bash","./njmon_installation.sh"]
