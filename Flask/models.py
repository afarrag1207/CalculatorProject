import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

# This module defines our classes which then becomes tables within our database.
# For example, the class Cats (cats) is the table name and each attribute becomes a column
# in that table. So the 'cats' table will have four columns id, name, price, breed.
class Cats(db.Model):
    __tablename__ = 'cats'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    breed = db.Column(db.String(100))
