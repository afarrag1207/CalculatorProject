from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pprint import pprint

# Creating an engine so the data can be stored in a local directoy
engine = create_engine('sqlite:////web/Sqlite-Data/sqlalchemy_example.db')

# loading the sqlalchemy base class
Base = declarative_base()


# Setting up the classes that create the record objects and define the schema

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    # creates the field to store the person id
    person_id = Column(Integer, ForeignKey('person.id'))
    # creates the relationship between the person and addresses.  backref adds a property to the Person class to retrieve addresses
    person = relationship("Person", backref="addresses")


# this creates all tables in the engine, equivalent to "create table"
Base.metadada.bind = engine

Base.metadada.bind = engine

# Creating the session
SQLSession = sessionmaker(bind=engine)
session = SQLSession()
session.commit()

