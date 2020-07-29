# Pull base image
FROM node:12.16.1-alpine as build-stage

# Set work directory
WORKDIR /app/frontend

# Install dependencies
COPY package.json package-lock.json /app/frontend/
RUN npm install

# Add the rest of the code
COPY . /app/frontend/
