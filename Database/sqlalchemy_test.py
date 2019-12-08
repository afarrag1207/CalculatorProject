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

# Inserting Data

new_person1 = Person(first_name = 'Ali',
                     last_name = 'Farrag',
                     username = 'afarrag',
                     email = 'af1207@gmail.com',
                     address = '689 Bergen ave',
                     town = 'Jersey City'
                     )
session.add(new_person1)

new_person2 = Person(first_name = 'Ola',
                     last_name = 'Farrag',
                     username = 'ofarrag',
                     email = 'ofarrag@gmail.com',
                     address = '101 carlton club dr',
                     town = 'Piscataway'
                     )
session.add(new_person2)

new_person3 = Person(first_name = 'Joe',
                     last_name = 'Smith',
                     username = 'Jsmith',
                     email = 'jsmith@gmail.com',
                     address = '58 duncan ave',
                     town = 'Jersey City'
                     )
session.add(new_person3)

new_person4 = Person(first_name = 'Tan',
                     last_name = 'lee',
                     username = 'tlee',
                     email = 'tlee@gmail.com',
                     address = '16 Pine St',
                     town = 'Dunellen'
                     )
new_person5 = Person(first_name = 'Kate',
                     last_name = 'Mill',
                     username = 'Kmill',
                     email = 'kMiill@gmail.com',
                     address = '10 Wood ave',
                     town = 'Newark'
                     )
new_person6 = Person(first_name = 'Tony',
                     last_name = 'Miller',
                     username = 'tmiller',
                     email = 'tmiller@example.com',
                     address = '1662 Kinney Street',
                     town = 'Wolfden'
                     )
session.add_all([new_person4, new_person5, new_person6])
session.commit()


# Inserting products

i1 = Item(name='Chair', cost_price=9.21, selling_price=10.81, quantity=5)
i2 = Item(name='Pen', cost_price=3.45, selling_price=4.51, quantity=3)
i3 = Item(name='Headphone', cost_price=15.52, selling_price=16.81, quantity=50)
i4 = Item(name='Travel Bag', cost_price=20.1, selling_price=24.21, quantity=50)
i5 = Item(name='Keyboard', cost_price=20.1, selling_price=22.11, quantity=50)
i6 = Item(name='Monitor', cost_price=200.14, selling_price=212.89, quantity=50)
i7 = Item(name='Watch', cost_price=100.58, selling_price=104.41, quantity=50)
i8 = Item(name='Water Bottle', cost_price=20.89, selling_price=25, quantity=50)

session.add_all([i1, i2, i3, i4, i5, i6, i7, i8])
session.commit()


