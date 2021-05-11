from flask import Flask # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class

app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@34.89.110.105:3306/sakila' # Set the connection string to connect to the database

db = SQLAlchemy(app)
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.string(30), nullable=False)
    
if __name__ == "__main__":
    app.run(debug=True)