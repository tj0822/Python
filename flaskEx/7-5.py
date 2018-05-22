server {
    … 중략 …
    location / {
        try_files $uri @flask_application
    }

    … 중략 …

    location @flask_application {
        include uwsgi_params;
        uwsgi_pass unix:/tmp/uwsgi_flask_sample.sock;
    }
}
