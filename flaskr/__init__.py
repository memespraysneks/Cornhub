from flask import Flask, redirect, render_template, url_for
from calendarpage import calendarpage
from adddelete import adddelete
from database import databaseAPI
from login import loginpage
from dbconnection import setup_db
from register import registerpage
from editevent import editevent

def create_app(test=False):
    app = Flask(__name__, instance_relative_config=True)
    
    # secret key for the form
    app.config['SECRET_KEY'] = "secret key"
    
    if test:
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["TEST_DB"] = True

    app.register_blueprint(calendarpage)
    app.register_blueprint(adddelete)
    app.register_blueprint(databaseAPI)
    app.register_blueprint(loginpage)
    app.register_blueprint(registerpage)
    app.register_blueprint(editevent)
    
    with app.app_context():
        setup_db()

    @app.route("/")
    def index():
        return render_template("index.html")

    return app


if __name__ == "__main__":
    create_app()