from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres@localhost:5432/oman'

db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__= 'Persons'
    id =db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

db.create_all()

@app.route('/')
def index():
    with app.app_context():
        return "Hello i am back"





if __name__=='__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=8089)
