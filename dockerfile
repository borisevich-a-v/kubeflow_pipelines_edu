from python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /preprocess

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY ./app/* .

EXPOSE 8000
CMD ["/bin/bash"]