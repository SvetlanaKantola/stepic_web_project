sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/gunicorn.d/wqunicorn -b '0.0.0.0:8080' hello:app
sudo /etc/init.d/nginx restart
