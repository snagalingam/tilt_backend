FROM nginx

# delete the initial config file
RUN rm /etc/nginx/conf.d/default.conf

# copy our config file
COPY default.conf /etc/nginx/conf.d/default.conf

# copy certificate files
WORKDIR /etc/nginx/ssl/
COPY certs/tiltstaging.crt /etc/nginx/ssl/tiltstaging.crt
COPY certs/tiltstaging.key /etc/nginx/ssl/tiltstaging.key

# Expose ports
EXPOSE 80
EXPOSE 443
