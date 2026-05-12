from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
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


#User model
class User(db.Model):
  id:Mapped[int] = mapped_column(primary_key=True)
  username: Mapped[str] 
  email:Mapped[str]
  password:Mapped[str]
  medications:Mapped[list["Medications"]] = relationship(backref="user")




@app.route("/")
def hello_world():
  return "Hello world"

if __name__ == '__main__':
  app.run(debug=True)