from flask_sqlalchemy_direct.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()