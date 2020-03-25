# Pull base image
FROM node:12

# Set work directory
WORKDIR /app/

# Install dependencies
COPY package.json yarn.lock /app/
RUN npm install

# Add rest of the client code
COPY . /app/

EXPOSE 3000

CMD npm start
