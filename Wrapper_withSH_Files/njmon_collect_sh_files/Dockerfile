FROM ubuntu:20.04

COPY . .
ADD njmon_collect.sh /njmon_collect.sh
USER root
RUN chmod +x njmon_collect.sh
ENTRYPOINT ["sh","njmon_collect.sh"]
