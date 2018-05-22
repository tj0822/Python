server {
    … 중략 …
    location = /sample { rewrite ^ /sample/; }
    location /sample {
        try_files $uri @flask_application
    }

    … 중략 …

    location @flask_application {
        include uwsgi_params;
        uwsgi_param SCRIPT_NAME /sample;
        uwsgi_modifier1 30;
        uwsgi_pass unix:/tmp/uwsgi_flask_sample.sock;
    }
}
