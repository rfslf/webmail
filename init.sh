sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo /etc/init.d/mysql restart
sudo rm /etc/gunicorn.d/test
#sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
#mysql -uroot -e "CREATE DATABASE askweb;"
#mysql -uroot -e "CREATE USER 'django'@'localhost' IDENTIFIED BY 'django';"
#mysql -uroot -e "GRANT ALL PRIVILEGES ON db_stepic_project.* TO 'django'@'localhost';"
#mysql -uroot -e "FLUSH PRIVILEGES;"
#/home/box/web/ask/manage.py syncdb
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
cd /home/box/web/ask/
gunicorn ask.wsgi:application --bind 0.0.0.0:8000 -D
