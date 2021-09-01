# Python version
FROM python:3.8

#
ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /app

# Copy requirements into the working directory and name it also requirements
COPY requirements.txt requirements.txt

# Configure server with commands
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt 