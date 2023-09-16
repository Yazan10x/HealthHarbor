#!/usr/bin/env python3

import logging
import os
import random
import time
from argparse import ArgumentParser, RawTextHelpFormatter

import psycopg2
from psycopg2.errors import SerializationFailure
import psycopg2.extras

from dotenv import load_dotenv

# creates the necessary tables

def create_item_table(conn):
    with conn.cursor() as cur:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS items (id UUID PRIMARY KEY, label VARCHAR(256), quantity INTEGER)"
        )
        logging.debug("create_item_table(): status message: %s",
                      cur.statusmessage)
    conn.commit()

def main():
    load_dotenv()
    opt = parse_cmdline()
    try:
        # Attempt to connect to cluster with connection string provided to
        # script. By default, this script uses the value saved to the
        # DATABASE_URL environment variable.
        # For information on supported connection string formats, see
        # https://www.cockroachlabs.com/docs/stable/connect-to-the-database.html.
        db_url = opt.dsn
        conn = psycopg2.connect(db_url, 
                                application_name="$ docs_simplecrud_psycopg2", 
                                cursor_factory=psycopg2.extras.RealDictCursor)
    except Exception as e:
        logging.fatal("database connection failed")
        logging.fatal(e)
        return
    create_item_table(conn)

    # Close communication with the database.
    conn.close()

def parse_cmdline():
    parser = ArgumentParser(description=__doc__,
                            formatter_class=RawTextHelpFormatter)

    parser.add_argument("-v", "--verbose",
                        action="store_true", help="print debug info")

    parser.add_argument(
        "dsn",
        default=os.getenv("DATABASE_URL"),
        nargs="?",
        help="""\
database connection string\
 (default: value of the DATABASE_URL environment variable)
            """,
    )

    opt = parser.parse_args()
    if opt.dsn is None:
        parser.error("database connection string not set")
    return opt

if __name__ == "__main__":
    main()
