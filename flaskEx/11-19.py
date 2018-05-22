from celery.result import ResultBase
from tasks import A

result = A.delay(10)
results = [v for v in result.collect() if not isinstance(v, (ResultBase, tuple))]