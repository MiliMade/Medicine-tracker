from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import os

DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]


#create the app
app = Flask(__name__)

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


#configure postgres database
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/medicine-tracker"

#initialize app with extension
db.init_app(app)



@app.route("/")
def hello_world():
  return "Hello world"

if __name__ == '__main__':
  app.run(debug=True)