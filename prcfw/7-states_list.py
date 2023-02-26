#!/usr/bin/python3

from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqldb://root:''@localhost/hbnb_dev_db2")

# Create a metadata object
metadata = MetaData()

# Reflect the structure of the database
metadata.reflect(bind=engine)

# Get the table object for mytable
mytable = Table('states', metadata, autoload=True, autoload_with=engine)

# Create a database session
Session = sessionmaker(bind=engine)
session = Session()

# Query the mytable table
result = session.query(mytable).all()

# Print the results
for row in result:
    print(row.name)

# Close the session
session.close()

