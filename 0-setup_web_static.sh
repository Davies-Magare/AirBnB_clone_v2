#!/usr/bin/env bash
#Install and configure Nginx
apt-get install nginx -y
service nginx start
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Hello Davies" > /data/web_static/releases/test/index.html
rm /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
echo "server {
   listen 80;
   listen [::]:80;
   root /var/www/html;
   index ret_file.html;

   location /redirect_me {
     return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
  }
   error_page 404 /custom_404.html;
   location = /custom_404.html {
    internal;
  }
  location /hbnb_static {
    alias /data/web_static/current/;
  }
}" > /etc/nginx/sites-available/default
service nginx restart
