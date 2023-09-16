#!/usr/bin/env python3

import logging


def create_item_table(cur):
    cur.execute(
        "CREATE TABLE IF NOT EXISTS items (id UUID PRIMARY KEY, label VARCHAR(256), quantity INTEGER)"
    )
    logging.debug("create_item_table(): status message: %s",
                    cur.statusmessage)

def delete_item_table(conn):
    with conn.cursor() as cur:
        cur.execute("DROP TABLE accounts")
        logging.debug("delete_accounts(): status message: %s",
                      cur.statusmessage)
    conn.commit()







def get_item(id, cur):
    cur.execute(
        f"SELECT * FROM items WHERE id = '{id}'"
    )
    logging.debug("get_item(): status message: %s",
                    cur.statusmessage)
    return cur.fetchall()
    
def get_items(query, cur):
    cur.execute(query)
    logging.debug("get_items(): status message: %s",
                    cur.statusmessage)
    return cur.fetchall()
    
def create_item(item, cur):
    print(item['label'])
    cur.execute(
        f"INSERT INTO items (id, label, quantity) VALUES ('{item['id']}', '{item['label']}', {item['quantity']})"
    )
    logging.debug("create_item(): status message: %s",
                    cur.statusmessage)
    return item
    
def update_item(id, item, cur):
    cur.execute(
        f"UPDATE items SET id = '{item['id']}', label = '{item['label']}', quantity = {item['quantity']} WHERE id = {id}"
    )
    logging.debug("create_item(): status message: %s",
                    cur.statusmessage)
    return item
    
def delete_item(id, cur):
    cur.execute(
        f"DELETE FROM items WHERE id = ${id}"
    )
    logging.debug("create_item_table(): status message: %s",
                    cur.statusmessage)
    return True
    

