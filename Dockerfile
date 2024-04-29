FROM python:3.10-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

RUN apt-get update && apt-get install -y \
    libmariadb-dev-compat \
    pkg-config \
    gcc\
    mariadb-client

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY wait-for-mariadb.sh /app/wait-for-mariadb.sh
RUN chmod +x /app/wait-for-mariadb.sh

COPY . /app/
