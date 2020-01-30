FROM ghabxph/jonkkins-python3

# Copy project source code
COPY src /app

# Copy config to image
COPY conf /conf

# WORKDIR to Source Code
WORKDIR /app

# Start the project
ENTRYPOINT '/usr/local/bin/python' 'dev.py'