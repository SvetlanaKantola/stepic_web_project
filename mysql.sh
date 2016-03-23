root rm /etc/nginx/sites-enabled/default
root service mysql start
mysql -uroot -e "CREATE DATABASE box"
