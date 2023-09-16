import os, sys
from argparse import ArgumentParser, RawTextHelpFormatter

import logging
import psycopg2
from psycopg2.errors import SerializationFailure
import psycopg2.extras

import json

from functions import *

from dotenv import load_dotenv

def get_cursor():
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
    
    with conn.cursor() as cur:


        # item =  '{ "id": "35998002-7e37-443f-ab43-e4ed7517dce3", "label":"s", "quantity":123}'
        # item_json = json.loads(item)
        # print(item_json)
        # create_item(item_json, cur)


        # add functions here

        q = get_item("35998002-7e37-443f-ab43-e4ed7517dce3", cur)
        print(q)
        print(json.dumps(q[0]))

    conn.commit()

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

get_cursor()