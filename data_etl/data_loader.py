import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
import structlog
from sqlalchemy import MetaData, Table, Column, Integer, String

# Define logger
logger = structlog.get_logger()


class DataLoader:
    def __init__(self, db_path, data):
        self.db_path = db_path
        self.data = data

    def load_data(self):
        # Connect to the SQLite database
        logger.info('Connecting to database')
        conn = sqlite3.connect(self.db_path)
        logger.info('Creating a SQL engine')
        engine = create_engine('sqlite:///' + self.db_path, echo=True)
        new_data_points = 0
        old_data_points = 0
        # metadata is the schema required for the table
        # Create or connect to the database and table
        metadata = MetaData()
        posts = Table(
            'posts', metadata,
            Column('id', Integer, primary_key=True),
            Column('title', String),
            Column('body', String),
            Column('title_length', Integer)
        )
        metadata.create_all(engine)
        logger.info('Loading data')
        with engine.connect() as connection:
            for index, row in self.data.iterrows():
                insert_query = posts.insert().values(
                    id=row['id'],
                    title=row['title'],
                    body=row['body'],
                    title_length=row['title_length']
                )
                try:
                    connection.execute(insert_query)
                    new_data_points += 1
                except IntegrityError:
                    logger.info('{} already exists'.format(row['title']))
                    # Upsert functionality being added here
                    update_query = posts.update().values(
                        title=row['title'],
                        body=row['body'],
                        title_length=row['title_length']
                    ).where(posts.c.id == row['id'])
                    connection.execute(update_query)
                    old_data_points += 1
            logger.info('Everything uploaded. Closing connection now. Have a nice day! :)')
            connection.commit()
        conn.close()
        return new_data_points, old_data_points
