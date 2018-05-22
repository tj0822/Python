@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('405.html'), 405