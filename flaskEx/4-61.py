def no_cache(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        resp = make_response(f(*args, **kwargs))
        h = resp.headers
        h['Last-Modified'] = datetime.datetime.now()
        h['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
        h['Pragma'] = 'no-cache'
       
        return resp
    return decorated_function