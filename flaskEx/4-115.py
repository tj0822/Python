@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    rv = make_response(jsonify(result=a + b))
    rv.headers.add('Access-Control-Allow-Origin', '*')
   
    return rv