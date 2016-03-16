sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/gunicorn.py /etc/gunicorn.d/ask.py
cd /home/box/web/ask/
sudo /etc/init.d/nginx restart
#sudo pip install --upgrade django
sudo rm /home/box/web/ask/la.log
sudo rm /home/box/web/ask/err.log
sudo gunicorn --bind 0.0.0.0:8000 --access-logfile /home/box/web/ask/la.log --error-logfile /home/box/web/ask/err.log ask.wsgi:application &
