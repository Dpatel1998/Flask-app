from app import db, Users

db.drop_all()
db.create_all()

testuser = Users(first_name='Dhruv',last_name='Patel') # Extra: this section populates the table with an example entry
db.session.add(testuser)
db.session.commit()