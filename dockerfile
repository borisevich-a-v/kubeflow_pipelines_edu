from python:3.9

RUN /usr/local/bin/python -m pip install --upgrade pip
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /preprocess
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY ./table_extractor/preprocess/* ./


EXPOSE 8000
CMD ["/bin/bash"]
