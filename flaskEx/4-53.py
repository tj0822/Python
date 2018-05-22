@app.route("/board_view")
@cached(timeout=10 * 60, key='board/%s')
def board_view():
    … 중략
    return render_template("/board_view.html")