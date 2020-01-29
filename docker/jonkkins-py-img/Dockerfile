FROM python:3.9.0a2-alpine3.10

# Install essential dependencies
RUN apk --no-cache add \
        alpine-sdk \
        libffi-dev \
        openssl-dev \
        postgresql-dev

# Install python requirements
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# 2020-01-29
RUN pip install pymongo