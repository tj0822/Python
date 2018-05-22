from flask import Flask, g, jsonify

app = Flask(__name__)

@app.route('/users/me')
def users_me():
    return jsonify(username=g.user.username)

if __name__ == "__main__":
    app.run()