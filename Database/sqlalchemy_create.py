# This Python file uses the following encoding: utf-8
import sqlite3

conn = sqlite3.connect('/web/Sqlite-Data/sqlalchemy_example.db')

c = conn.cursor()
c.execute('''
          CREATE TABLE Person
          (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
          ''')
c.execute('''
          CREATE TABLE Address
          (id INTEGER PRIMARY KEY ASC, street_name varchar(250), street_number varchar(250),
           post_code varchar(250) NOT NULL, person_id INTEGER NOT NULL,
           FOREIGN KEY(person_id) REFERENCES person(id))
          ''')
c.execute('''
          CREATE TABLE Item
          (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
          ''')
c.execute('''
          CREATE TABLE Order 
          (id INTEGER PRIMARY KEY ASC, Line_item1 varchar(250), Line_item2 varchar(250),
           Line_item3 varchar(250) NOT NULL, person_id INTEGER NOT NULL,
           FOREIGN KEY(item_id) REFERENCES item(id))
         ''')

c.execute('''
          INSERT INTO person VALUES(1, 'pythoncentral')
          ''')
c.execute('''
          INSERT INTO address VALUES(1, 'python road', '1', '00000', 1)
          ''')

conn.commit()
conn.close()