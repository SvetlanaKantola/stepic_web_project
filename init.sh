sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
#sudo /etc/gunicorn.d/wqunicorn -c '0.0.0.0:8080' hello:app
sudo gunicorn -c /home/box/web/etc/gunicorn.conf --debug -D hello:wsgi_app
sudo /etc/init.d/nginx restart
