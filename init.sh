sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo rm -r /etc/gunicorn.d/*
sudo ln -sf /home/box/web/etc/gunicorn.py /etc/gunicorn.d/qa.py
cd /home/box/web/ask/
sudo /etc/init.d/nginx restart
#sudo pip install --upgrade gunicorn
#sudo pip install --upgrade django
sudo rm /home/box/web/ask/la.log
sudo rm /home/box/web/ask/err.log
#sudo gunicorn -c /etc/gunicorn.d/test -D --bind 0.0.0.0:8000 --access-logfile /home/box/web/ask/la.log --error-logfile /home/box/web/ask/err.log ask.wsgi:application &
sudo /etc/init.d/gunicorn restart
sudo rm -r /etc/mysql/my.cnf
sudo ln -sf /home/box/web/etc/my.cnf  /etc/mysql/my.cnf
sudo /etc/init.d/mysql start

mysql -uroot -e "CREATE DATABASE qa"
mysql -uroot -e "CREATE USER 'boxuser'@'localhost' IDENTIFIED BY '1234';
				 GRANT ALL ON qa.* TO 'boxuser'@'localhost';"

sudo python /home/box/web/ask/manage.py syncdb