sudo service mysql start
mysql -uroot -e "create database if not exists qabdsk"
mysql -uroot -e "create user 'qask'@'localhost' IDENTIFIED BY '345345'"
mysql -uroot -e "GRANT ALL PRIVILEGES ON qabdsk.* TO 'qask'@'localhost'"

python ./manage.py syncdb