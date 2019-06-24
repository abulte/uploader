FROM alpine:3.4
ENV NGINX_VERSION 1.13.6

COPY install.sh /usr/src/
COPY nginx.key /usr/src/

RUN sh -x /usr/src/install.sh

COPY nginx.conf /etc/nginx/nginx.conf
COPY nginx.vh.default.conf /etc/nginx/conf.d/default.conf

# Create temporary upload locations
# no need when docker volumes are mounted
#RUN mkdir -p /var/www/_files
# TODO :thinking:
#RUN chmod 777 -R /var/www/_files

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
