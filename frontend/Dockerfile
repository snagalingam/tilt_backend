# Stage 0: "build-stage" to build and compile frontend
# Pull base image
FROM node:12.16.1-alpine as build-stage

# Set work directory
WORKDIR /app/frontend

# Install dependencies
COPY package.json yarn.lock /app/frontend/
RUN yarn

# Add the rest of the code
COPY . /app/frontend/

# Build static files
RUN yarn build

# Stage 1: based on Nginx, to have only the compiled app, ready for production with Nginx
FROM nginx:1.15

COPY --from=build-stage /app/frontend/build/ /usr/share/nginx/html

COPY --from=build-stage /app/frontend/default.conf.template /etc/nginx/conf.d/default.conf.template
