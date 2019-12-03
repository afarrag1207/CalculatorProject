from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import create_engine

engine = create_engine("sqlite:////web/sqlalchemy_example.db")
Session = sessionmaker(bind=engine)
session = Session()
