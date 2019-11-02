FROM nginx:latest

RUN rm /etc/nginx/nginx.conf
RUN rm -rf /etc/nginx/conf.d/

COPY nginx.conf /etc/nginx/
COPY conf.d/ /etc/nginx/conf.d
COPY nginx_ssl_conf/nginx-selfsigned.crt /etc/ssl/certs/
COPY nginx_ssl_conf/nginx-selfsigned.key /etc/ssl/private/
COPY nginx_ssl_conf/dhparam.pem /etc/ssl/certs/
