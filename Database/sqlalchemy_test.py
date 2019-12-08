from sqalchemy import Column, Foreignkey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from pprint import pprint

# The sqlalchemy_example.db file is an engine that stores data in the local directory's
engine = create_engine('sqlite:////web/SQL-Data/sqalchemy_example.db')

# this loads the sqlalchemy base class
Base = declarative_base()


# Setting up the classes to create the record objects and define the Schema

class Client(Base):
    __tablename__ = 'Client'
    # Here we define columns for the table client
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = 'address'
    # We are defining columns for the table address
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(Integer, Foreignkey('person.id'))
    # creating the relationship between the client and addresses.
    # backref adds a property to the client class to retrive addresses
    client = relationship('Client', backref="addresses")


Base.metadata.create_all(engine)
Base.metadata.bind = engine

# Creating the session
SQLDBSession = sessionmaker(bind=engine)

session = SQLDBSession()
session.commit()


