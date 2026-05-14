from typing import Optional
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import date, datetime
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
  medications:Mapped[list["Medication"]] = relationship(backref="user")

#Medication model
class Medication (db.Model):
    id: Mapped[int]
    name: Mapped[str]
    dosage: Mapped[str]
    frequency: Mapped[str]
    created_at: Mapped[date] = mapped_column(nullable=False, default=datetime.timezone.utc)
    start_date: Mapped[date]
    end_date: Mapped[Optional[date]] = mapped_column(nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    notes:Mapped[Optional[str]] = mapped_column(nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))






@app.route("/")
def hello_world():
  return "Hello world"

if __name__ == '__main__':
  app.run(debug=True)