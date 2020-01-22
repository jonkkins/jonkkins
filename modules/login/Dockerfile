FROM python:3.9.0a2-alpine3.10

# Install essential dependencies
RUN apk add alpine-sdk
RUN apk add libffi-dev

# Upgrade pip
RUN pip install pip==20.0.1

# Install all project dependencies
RUN pip install Flask==1.1.1
RUN pip install bcrypt==3.1.7

# Copy project source code
COPY src /app

# WORKDIR to Source Code
WORKDIR /app

# Start the project
ENTRYPOINT '/usr/local/bin/python' 'dev.py'