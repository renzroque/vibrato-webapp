FROM ubuntu:trusty
MAINTAINER renzmroq@gmail.com

RUN apt-get update -y && \
  apt-get install -y python3-pip apache2 libapache2-mod-wsgi-py3 libmysqlclient-dev

COPY vibrato_project /var/www/html/vibrato_project && \
  apache2.conf /etc/apache2/sites-available/000-default.conf

WORKDIR /var/www/html/vibrato_project

RUN pip3 install django && \
  pip3 install mysqlclient && \
  pip3 install Faker

EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

