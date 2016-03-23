sudo pip install --upgrade django
sudo /etc/init.d/mysql restart
sudo mysql -uroot -e  "CREATE DATABASE qa"
sudo mysql -uroot -e  "CREATE USER 'box'@'localhost' IDENTIFIED BY 'box'"
sudo mysql -uroot -e  "GRANT ALL PRIVILEGES ON * . * TO 'box'@'localhost'"
python ask/manage.py makemigrations
python ask/manage.py migrate

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/hello /etc/gunicorn.d/hello
sudo ln -sf /home/box/web/etc/ask /etc/gunicorn.d/ask

sudo /etc/init.d/gunicorn restart
