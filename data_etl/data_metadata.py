from sqlalchemy import MetaData, Table, Column, Integer, String
# Define the schema for the metadata being used in data_loader.py
metadata = MetaData()
posts = Table(
    'posts', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('body', String),
    Column('title_length', Integer)
)