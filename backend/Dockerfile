# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app/backend

# Install dependencies
COPY Pipfile Pipfile.lock /app/backend/
RUN pip install pipenv && pipenv install --system

# Add the rest of the code
COPY . /app/backend/
