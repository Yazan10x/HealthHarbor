#!/usr/bin/env python3

import logging, json



def get(query) -> dict:
    pass



def create_item_table(cur) -> None:
    cur.execute(
        "CREATE TABLE IF NOT EXISTS items (id UUID PRIMARY KEY, label VARCHAR(256), quantity INTEGER)"
    )
    logging.debug("create_item_table(): status message: %s",
                    cur.statusmessage)

def delete_item_table(cur) -> None:
    cur.execute("DROP TABLE accounts")
    logging.debug("delete_accounts(): status message: %s",
                    cur.statusmessage)




def get_item(id, cur) -> str:
    cur.execute(
        f"SELECT * FROM items WHERE id = '{id}'"
    )
    logging.debug("get_item(): status message: %s",
                    cur.statusmessage)
    
    # assume get_item always returns exactly one entry
    return json.dumps(cur.fetchone())


def get_items(query, cur) -> [str]:
    cur.execute(query)
    logging.debug("get_items(): status message: %s",
                    cur.statusmessage)
    items = []
    for dict in cur.fetchall():
        items.append(json.dumps(dict))
    
    return items
    
def create_item(item, cur) -> dict:
    print(item['label'])
    cur.execute(
        f"INSERT INTO items (id, label, quantity) VALUES ('{item['id']}', '{item['label']}', {item['quantity']})"
    )
    logging.debug("create_item(): status message: %s",
                    cur.statusmessage)
    
    # assume create item will always create one entry
    return item
    
def update_item(id, item, cur) -> dict:
    cur.execute(
        f"UPDATE items SET id = '{item['id']}', label = '{item['label']}', quantity = {item['quantity']} WHERE id = {id}"
    )
    logging.debug("create_item(): status message: %s",
                    cur.statusmessage)
    
    # assume update_item will always update one entry
    return item
    
def delete_item(id, cur) -> bool:
    cur.execute(
        f"DELETE FROM items WHERE id = ${id}"
    )
    logging.debug("create_item_table(): status message: %s",
                    cur.statusmessage)
    
    # assume delete_item will always delete one entry
    return True
    

