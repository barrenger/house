#from flask import Flask
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
app = Flask(__name__)

def create_app():
    app.debug=True
    app.secret_key='1721c20f1efb44b3675c42beb7fda902'

    #set the app configuration data 
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///house.sqlite'

    #initialize db with flask app
    db.init_app(app)

    bootstrap = Bootstrap(app)

    #importing modules here to avoid circular references, register blueprints of routes
    from . import views
    app.register_blueprint(views.bp)

    return app



@app.errorhandler(404) 
# inbuilt function which takes error as parameter 
def not_found(e): 
  return render_template("404.html")

@app.errorhandler(500)
def internal_error(e):
  return render_template("500.html")
