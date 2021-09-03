# Python version
FROM python:3.8

#
ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /app

# Copy requirements into the working directory and name it also requirements
COPY requirements.txt requirements.txt

# Configure server with commands
RUN pip3 install -r requirements.txt

# docker hub stuff
# EXPOSE 8000

# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "core.wsgi:application"]

# heroku stuff
#CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT