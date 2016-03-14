sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
#sudo gunicorn -b '0.0.0.0:8080' hello:app &
#sudo /etc/init.d/gunicorn restart -c /home/box/web/etc/gunicorn.conf --debug -D hello:wsgi_app
#sudo ln -sf /home/box/web/etc/gunicorn.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/gunicorn.py /etc/gunicorn.d/ask.py
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/nginx restart
#sudo gunicorn -c /etc/gunicorn.d/hello.py --debug -D hello
#django-admin startproject ask
#gunicorn ask.wsgi:application --bind 0.0.0.0:8000 &
