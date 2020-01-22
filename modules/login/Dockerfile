FROM python:3.9.0a2-alpine3.10

# Run initial setup
COPY ./setup/initial.sh /
RUN sh initial.sh

# Copy project source code
COPY src /app

# WORKDIR to Source Code
WORKDIR /app

# Start the project
ENTRYPOINT '/usr/local/bin/python' 'dev.py'