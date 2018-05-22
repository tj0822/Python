@celery.task(bind=True)
def add_python_flask(self):
    return sum(range(11))