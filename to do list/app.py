from flask import Flask
from flask sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@34.89.110.105:3306/sakila'

db = SQLAlchemy(app)

class todos(db.Model):
    id = db.Column(db.Intenger, primary_key=True)
    task = db.Colume(db.Boolean, nullable=False)
    complete = db.Colume(db.Boolean, default=False)

@app.route("/")
def index():
    return "This is a TODO App"

if __name__ == "__mail__":
    app.run(debug=true, host='0.0.0.0')
