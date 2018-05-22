@app.route("/")
@templated("development/hello_new.html")
def hello_new():
    return dict(value=1)