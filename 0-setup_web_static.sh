#!/usr/bin/env bash
#install nginx
apt-get install nginx -y
sudo service nginx start
#make directories and test file
mkdir /data/ 2>/dev/null
mkdir -p /data/web_static/ 2>/dev/null
mkdir -p /data/web_static/releases 2>/dev/null
mkdir -p /data/web_static/shared 2>/dev/null
mkdir -p /data/web_static/releases/test/ 2>/dev/null
echo "Hello World" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
echo "server {
   listen 80;
   listen [::]:80;
   root /var/www/html;
   index ret_file.html;

   location / {
   add_header X-Served-By 79879-web-01;
   }

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
}" > /etc/nginx/sites-enabled/default

sudo service nginx restart
