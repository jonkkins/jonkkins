FROM php:7.4.2-apache-buster

# Initial setup
RUN mkdir -p /var/www/html/public
COPY php/apache/sites-available /etc/apache2/sites-available
COPY php/init.sh /init.sh
RUN chmod 755 /init.sh
