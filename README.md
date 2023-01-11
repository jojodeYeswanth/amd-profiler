# amd-profiler
This repo contains the code for wrapper(Data Collector) component of the profiling tool Creating wrapper directory Collecting data using njomn for workload profiler. Renaming the workload profiler file and removing the .err file Commands to collect cpu, memory, disks, Network details Making Dictionary of all above commands. Creating Json File of the dictionary And finally creates Tar file of the wrapper folder

FROM python:3

COPY . .
RUN apt update && apt install python3-pip
RUN pip3 install -r requirement.txt
ADD njmon_installation.sh /

RUN bash -c "/njmon_installtion.sh"
ADD njmon_collect.sh /
RUN bash -c "/njmon_collect.sh"
EXPOSE 8080

ENTRYPOINT ["python3"]
CMD ["wrapper.py"]