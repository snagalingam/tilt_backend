# Pull base image
FROM node:12.16.1-alpine

# Set work directory
WORKDIR /app/frontend

# Install dependencies
COPY package.json yarn.lock /app/frontend/
RUN yarn install

# Add the rest of the code
COPY . /app/frontend/

# Build static files
RUN yarn build

# Have to move all static files other than index.html to root
# for whitenoise middleware
WORKDIR /app/frontend/build
RUN mkdir root && mv *.ico *.js *.json root
