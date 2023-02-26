#!/usr/bin/python3

from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
from flask import Flask, render_template

engine = create_engine("mysql+mysqldb://root:''@localhost/hbnb_dev_db2")
metadata = MetaData()
metadata.reflect(bind=engine)

mytable = Table('states', metadata, autoload=True, autoload_with=engine)

Session = sessionmaker(bind=engine)
session = Session()

result = session.query(mytable).all()

#for row in result:
 #   print(row.name)

#session.close()

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def list_states():
    result = session.query(mytable).all()
    return renbder_template('7s.html', r=result)

@app.teardown_appcontext
def tear_down_db(execute):
    storage.close()

