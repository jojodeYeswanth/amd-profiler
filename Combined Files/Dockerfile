FROM python:3.8
ENV USER root
WORKDIR /
COPY . .
RUN apt-get update && apt-get install -y python3-pip && apt-get -y install sudo && apt-get install -y wget && apt-get install -y apt-utils && apt-get install -y curl

RUN apt update && apt install -y python3-pip
RUN pip install -r requirement.txt
CMD ["python", "app.py"]
