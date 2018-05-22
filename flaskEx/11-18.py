from celery import group
from main import celery

@celery.task(trail=True)
def A(how_many):
    return group(B.s(i) for i in range(how_many))()

@celery.task(trail=True)
def B(i):
    return pow2.delay(i)

@celery.task(trail=True)
def pow2(i):
    return i ** 2