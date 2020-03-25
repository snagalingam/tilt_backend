# Pull base image
FROM node:12.16.1-alpine

# Set work directory
WORKDIR /app/frontend

# Install dependencies
COPY package.json yarn.lock /app/frontend/
RUN yarn

# Add the rest of the code
COPY . /app/frontend/
