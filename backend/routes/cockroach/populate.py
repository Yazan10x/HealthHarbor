import logging
import pandas as pd
from routes.cockroach.conn import *
from routes.cockroach.health_items import create_item, delete_item_table, create_item_table

def populate() -> int:
    print("deleting table...")
    delete_item_table()
    print("creating new empty table...")
    create_item_table()
    data = pd.read_csv('backend/routes/cockroach/drugs_info_count.csv')
    dict_data = data.to_dict('records')
    count = 0
    print("now populating table...")
    conn = get_conn()
    with conn.cursor() as cur:
        for item in dict_data:
            print(f"populated {count} entries")
            create_item(item)
            count += 1
        logging.debug("populate(): status message: %s",
                        cur.statusmessage)
    conn.commit()
    print("finished populating table!")
    close_conn(conn)

    # assume create item will always create one entry
    return count