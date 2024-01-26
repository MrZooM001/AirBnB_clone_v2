#!/usr/bin/env bash
# Prepare your web servers
sudo apt-get update
sudo apt-get -y install nginx
sudo service nginx start

root_path="/data/web_static"
html_content="<html><head></head><body>Hello to this website!!!</body></html>"
mkdir -p "$root_path/releases/test"
mkdir -p "$root_path/shared"
echo -e "$html_content" | sudo tee $root_path/releases/test/index.html
sudo rm -r "$root_path/current"
sudo ln -sf $root_path/releases/test/ $root_path/current
chown -Rh "ubuntu:ubuntu" "/data/"

ngx_cfg_file="/etc/nginx/sites-enabled/default"
sed -i "/server_name _;/a\\        location /hbnb_static/ {alias $root_path/current/;}" "$ngx_cfg_file" > /dev/null
sudo service nginx restart
