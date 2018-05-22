class _AddTask(celery.Task):
    def run(self, x, y):
        return x + y

add = celery.tasks[_AddTask.name]