# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app/

# Install dependencies
COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --system

# Add the rest of the code
COPY . /app/

# SECRET_KEY is only included here to avoid raising an error when generating static files.
# Be sure to add a real SECRET_KEY config variable in deployment.
RUN SECRET_KEY=somethingsupersecret \
  python3 manage.py collectstatic --noinput

EXPOSE $PORT
