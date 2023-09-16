import os

import logging
import psycopg2
import psycopg2.extras

from dotenv import load_dotenv

def get_conn():
    load_dotenv()
    try:

        # Attempt to connect to cluster with connection string provided to
        # script. By default, this script uses the value saved to the
        # DATABASE_URL environment variable.
        # For information on supported connection string formats, see
        # https://www.cockroachlabs.com/docs/stable/connect-to-the-database.html.

        db_url = os.getenv("DATABASE_URL")
        conn = psycopg2.connect(db_url, 
                                application_name="$ docs_simplecrud_psycopg2", 
                                cursor_factory=psycopg2.extras.RealDictCursor)
    except Exception as e:
        logging.fatal("database connection failed")
        logging.fatal(e)
        return
    
    return conn
    
def close_conn(conn) -> None:
    conn.close()