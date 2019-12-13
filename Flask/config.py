import os

# This modules only job at the moment is to generate this URI, but could easily be extended to add extra configuration varibales if required
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_PASSWORD']
database = os.environ['POSTGRES_DB']
port = os.environ['POSTGRES_PORT']

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'

# NOTE: F-strings used for formatting strings (as shown above) can only be used with Python3.6


