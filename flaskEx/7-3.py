WSGIDaemonProcess hello_world user=www-data group=www-data threads=5
WSGIScriptAlias /sample /var/www/html/sample/hello_world.wsgi

<Directory /var/www/html/sample>
    WSGIProcessGroup hello_world
    WSGIApplicationGroup %{GLOBAL}
    Order deny,allow
    Allow from all
</Directory>
