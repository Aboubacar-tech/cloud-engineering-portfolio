sh-4.2$ systemctl status httpd
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; vendor preset: disabled)
   Active: active (running) since Thu 2026-07-09 20:55:18 UTC; 1h 43min ago
     Docs: man:httpd.service(8)
 Main PID: 11124 (httpd)
   Status: "Total requests: 435; Idle/Busy workers 100/0;Requests/sec: 0.0702; Bytes served/sec: 1.3KB/sec"
   CGroup: /system.slice/httpd.service
           ├─11124 /usr/sbin/httpd -DFOREGROUND
           ├─11125 /usr/sbin/httpd -DFOREGROUND
           ├─11126 /usr/sbin/httpd -DFOREGROUND
           ├─11127 /usr/sbin/httpd -DFOREGROUND
           ├─11128 /usr/sbin/httpd -DFOREGROUND
           ├─11129 /usr/sbin/httpd -DFOREGROUND
           ├─11202 /usr/sbin/httpd -DFOREGROUND
           └─11205 /usr/sbin/httpd -DFOREGROUND
sh-4.2$ ls /var/www/html
css  cv  image  images  index.html  js  LICENSE  README.md
sh-4.2$ curl localhost
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Portfolio professionnel de développeur web - ABOUTECH">
  <meta name="author" content="Aboubacar">
  <meta property="og:title" content="Portfolio Aboutech">
  <meta property="og:description" content="Découvrez mes projets, compétences et parcours en développement web.">
  <meta property="og:image" content="images/ma-photo.webp">
  <meta property="og:type" content="website">
  <title>Portfolio - ABOUTECH</title>
 
sh-4.2$ systemctl status httpd
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; vendor preset: disabled)
   Active: active (running) since Thu 2026-07-09 20:55:18 UTC; 1h 43min ago
     Docs: man:httpd.service(8)
 Main PID: 11124 (httpd)
   Status: "Total requests: 435; Idle/Busy workers 100/0;Requests/sec: 0.0702; Bytes served/sec: 1.3KB/sec"
   CGroup: /system.slice/httpd.service
           ├─11124 /usr/sbin/httpd -DFOREGROUND
           ├─11125 /usr/sbin/httpd -DFOREGROUND
           ├─11126 /usr/sbin/httpd -DFOREGROUND
           ├─11127 /usr/sbin/httpd -DFOREGROUND
           ├─11128 /usr/sbin/httpd -DFOREGROUND
           ├─11129 /usr/sbin/httpd -DFOREGROUND
           ├─11202 /usr/sbin/httpd -DFOREGROUND
           └─11205 /usr/sbin/httpd -DFOREGROUND
sh-4.2$ ls /var/www/html
css  cv  image  images  index.html  js  LICENSE  README.md
sh-4.2$ curl localhost
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Portfolio professionnel de développeur web - ABOUTECH">
  <meta name="author" content="Aboubacar">
  <meta property="og:title" content="Portfolio Aboutech">
  <meta property="og:description" content="Découvrez mes projets, compétences et parcours en développement web.">
  <meta property="og:image" content="images/ma-photo.webp">
  <meta property="og:type" content="website">
  <title>Portfolio - ABOUTECH</title>
  <link rel="icon" href="favicon.ico">



sh-4.2$ mysql -h production-mysql.ccxwywsk4n3x.us-east-1.rds.amazonaws.com -u admin -p
Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 73
Server version: 8.0.46 Source distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [(none)]> admin
    ->





