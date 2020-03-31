# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install curl, node, & yarn
RUN apt-get -y install curl \
  && curl -sL https://deb.nodesource.com/setup_12.x | bash \
  && apt-get install nodejs \
  && curl -o- -L https://yarnpkg.com/install.sh | bash

# Set work directory
WORKDIR /app/backend

# Install dependencies
COPY ./backend/Pipfile ./backend/Pipfile.lock /app/backend/
RUN pip install pipenv && pipenv install --system

# Set work directory
WORKDIR /app/frontend

# Install JS dependencies
COPY ./frontend/package.json ./frontend/yarn.lock /app/frontend/
RUN yarn

# Add the rest of the code
COPY . /app/

# Build static files
RUN yarn build

# Have to move all static files other than index.html to root
# for whitenoise middleware
WORKDIR /app/frontend/build
RUN mkdir root && mv *.ico *.js *.json root

# Set to main working directory
WORKDIR /app
