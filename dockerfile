from python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /badgerdoc

COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

COPY ./badgerdoc/config.py ./config.py
WORKDIR /badgerdoc/preprocess
COPY ./badgerdoc/preprocess/* ./


EXPOSE 8000
CMD ["/bin/bash"]
