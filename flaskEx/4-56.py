@app.route("/", endpoint="production.hello")
@templated()
def hello():
    return dict(value=1)