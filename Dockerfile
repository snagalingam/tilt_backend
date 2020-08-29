# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT 'development'
ENV DATABASE_HOST 'tiltpostgresdev.co1g8hkhkrwp.us-east-2.rds.amazonaws.com'
ENV DATABASE_NAME 'tiltpostgresdev'
ENV DATABASE_PASSWORD 'tiltpostgresdev'
ENV DATABASE_USER 'tiltpostgresdev'
ENV DEBUG 1
ENV SECRET_KEY '((5qzn4=1s57*63r48lqkvz%60d#&_@b4w5f05$$6)lu35r(^lm'

# Set working directory
WORKDIR /app/

# Install Python dependencies
COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --system

# Add the rest of the code
COPY . /app/

# SECRET_KEY is only included here to avoid raising an error when generating static files.
# Be sure to add a real SECRET_KEY config variable in deployment.
RUN SECRET_KEY=somethingsupersecret \
  python3 manage.py collectstatic --noinput

EXPOSE $PORT
