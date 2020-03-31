# Stage 0: "build-stage" to build and compile frontend
# Pull base image
FROM node:12.16.1-alpine as build-stage

# Set work directory
WORKDIR /app/frontend

# Install dependencies
COPY ./frontend/package.json ./frontend/yarn.lock /app/frontend/
RUN yarn

# Add the rest of the code
COPY ./frontend /app/frontend/

# Build static files
RUN yarn build

# Stage 1: Compile the app and ready for production
# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app/backend

# Install dependencies
COPY ./backend/Pipfile ./backend/Pipfile.lock /app/backend/
RUN pip install pipenv && pipenv install --system

# Add the rest of the code
COPY . /app/
COPY --from=build-stage /app/frontend/build/ /app/frontend/build/

# Have to move all static files other than index.html to root/
# for whitenoise middleware
WORKDIR /app/frontend/build
RUN mkdir root && mv *.ico *.js *.json root

WORKDIR /app

# SECRET_KEY is only included here to avoid raising an error when generating static files.
# Be sure to add a real SECRET_KEY config variable in Heroku.
RUN SECRET_KEY=somethingsupersecret \
  python /app/backend/manage.py collectstatic --noinput
RUN python /app/backend/manage.py makemigrations
RUN python /app/backend/manage.py migrate
