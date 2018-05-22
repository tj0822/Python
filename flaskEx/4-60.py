def role(role):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # args의 값과 session의 access_auth 값과 비교하여 접근할 수 없는 경우 이전 페이지로 돌려보낸다.
            # 접근권한의 기본값은 검색이다.
            if role not in session.get("access_auth", "S"):
                flash(u'허가되지 않은 사용자입니다')
                return redirect(request.referrer)
            return f(*args, **kwargs)
        return decorated_function
    return wrapper