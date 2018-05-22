from imaginary_twitter_lib import Twitter

@celery.task(bind=True)
def tweet(self, auth, message):
    twitter = Twitter(oauth=auth)
    try:
        twitter.post_status_update(message)
    except twitter.FailWhale as exc:
        # Retry in 5 minutes.
        raise self.retry(countdown=60 * 5, exc=exc)