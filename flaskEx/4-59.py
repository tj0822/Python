def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # 로그인 아이디가 존재하지 않으면 로그인 페이지로 돌려보낸다.
        if session.get("usr_id", None) is None:
            return redirect(url_for('member_page.loginForm', next=request.url))
        # 로그인 권한이 충분한지 확인한다
        if "R" not in session["access_auth"]:
            # 검색 시스템으로 돌려보낸다.
            return redirect(url_for("home./"))
        return f(*args, **kwargs)
    return decorated_function