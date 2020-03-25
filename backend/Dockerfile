# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code/backend

# Install dependencies
COPY Pipfile Pipfile.lock /code/backend/
RUN pip install pipenv && pipenv install --system

# Add the rest of the code
COPY . /code/backend/
