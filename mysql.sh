mysql -uroot -e "CREATE DATABASE askweb;"
mysql -uroot -e "GRANT ALL PRIVILEGES ON askweb.* TO 'box'@'localhost' WITH GRANT OPTION;"
mysql -uroot -e "GRANT ALL PRIVILEGES ON askweb.* TO 'x'@'localhost' WITH GRANT OPTION;"
