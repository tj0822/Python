[uwsgi]
touch-reload=/tmp/flask_sample.app
socket = /tmp/uwsgi_flask_sample.sock
workers = 2
chdir = /var/www/html/sample
callable = app
module = hello_world
uid = 33
gid = 33
venv = /var/www/sample_edition
