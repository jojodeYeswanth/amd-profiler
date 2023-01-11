FROM ubuntu:20.04

COPY . .
ADD njmon_installation.sh /njmon_installation.sh
USER root
RUN apt-get update && apt-get install -y python3-pip && apt-get -y install sudo && apt-get install -y wget && apt-get install -y apt-utils && apt-get install -y curl
RUN pip3 install -e .
RUN chmod +x njmon_installation.sh
ENTRYPOINT ["sh","njmon_installation.sh"]
