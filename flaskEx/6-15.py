@app.route('/users/me')
def users_me():
    return jsonify(username=g.user.username)