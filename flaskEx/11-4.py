app.config.update(
    CELERY_BROKER_URL='sqla+postgresql+ pypostgresql://user:pass@localhost/dbname’,
    CELERY_RESULT_BACKEND='db+postgresql+pypostgresql://user:pass@localhost/dbname',
    CELERY_RESULT_ENGINE_OPTIONS={'echo': True}
)