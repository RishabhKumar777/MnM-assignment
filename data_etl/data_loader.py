import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from data_metadata import metadata, posts
import structlog

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
        logger.info('Creating a SQL engine using sqlite')
        engine = create_engine('sqlite:///' + self.db_path, echo=True)
        # metadata is the schema required for the table
        # Create or connect to the database and table
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
                except IntegrityError:
                    logger.info('{} already exists'.format(row['title']))
                    # Upsert functionality being added here
                    update_query = posts.update().values(
                        title=row['title'],
                        body=row['body'],
                        title_length=row['title_length']
                    ).where(posts.c.id == row['id'])
                    connection.execute(update_query)
        logger.info('Everything uploaded. Closing connection now. Have a nice day! :)')
        conn.close()
