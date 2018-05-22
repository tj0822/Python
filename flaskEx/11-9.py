from celery import Task

class DebugTask(Task):
    abstract = True

    def after_return(self, *args, **kwargs):
        print('Task returned: {0!r}'.format(self.request))


@app.task(base=DebugTask)
def add(x, y):
    return x + y