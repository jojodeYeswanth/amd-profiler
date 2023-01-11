FROM python:3.8.10

COPY . .
RUN apt-get update
RUN pip install -r requirement.txt
CMD ["python", "wrapper.py"]
