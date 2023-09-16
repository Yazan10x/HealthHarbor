import logging, json
from conn import *

def create_item_table() -> None:
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS items (id UUID PRIMARY KEY, label VARCHAR(256), quantity INTEGER)"
        )
        logging.debug("create_item_table(): status message: %s",
                        cur.statusmessage)
    conn.commit()
    close_conn(conn)

def delete_item_table() -> None:
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("DROP TABLE accounts")
        logging.debug("delete_item_table(): status message: %s",
                        cur.statusmessage)
    conn.commit()
    close_conn(conn)





def get_item(id) -> str:
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(
            f"SELECT * FROM items WHERE id = '{id}'"
        )
        logging.debug("get_item(): status message: %s",
                        cur.statusmessage)
        
        # assume get_item always returns exactly one entry
        item = json.dumps(cur.fetchone())
    conn.commit()
    close_conn(conn)

    return item


def get_items(query) -> [str]:
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(query)
        logging.debug("get_items(): status message: %s",
                        cur.statusmessage)
        items = [json.dumps(dict) for dict in cur.fetchall()]
    conn.commit()
    close_conn(conn)

    return items
    
def create_item(item) -> dict:
    conn = get_conn()
    with conn.cursor() as cur: 
        cur.execute(
            f"INSERT INTO items (id, label, quantity) VALUES ('{item['id']}', '{item['label']}', {item['quantity']})"
        )
        logging.debug("create_item(): status message: %s",
                        cur.statusmessage)
    conn.commit()
    close_conn(conn)

    # assume create item will always create one entry
    return item
    
def update_item(id, item) -> dict:
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(
            f"UPDATE items SET id = '{item['id']}', label = '{item['label']}', quantity = {item['quantity']} WHERE id = '{id}'"
        )
        logging.debug("update_item(): status message: %s",
                        cur.statusmessage)
    conn.commit()
    close_conn(conn)

    # assume update_item will always update one entry
    return item
    
def delete_item(id) -> bool:
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(
            f"DELETE FROM items WHERE id = '{id}'"
        )
        logging.debug("delete_item(): status message: %s",
                        cur.statusmessage)
    conn.commit()
    close_conn(conn)

    # assume delete_item will always delete one entry
    return True
    

# tests

item =  '{ "id": "35998002-7e37-443f-ab43-e4ed7517dce3", "label":"hello hello!", "quantity":1}'
item_json = json.loads(item)
create_item(item_json)

print(get_items('SELECT * FROM items'))
print(get_item('35998002-7e37-443f-ab43-e4ed7517dce3'))

item =  '{ "id": "35998002-7e37-443f-ab43-e4ed7517dce3", "label":"asasas", "quantity":222}'
item_json = json.loads(item)
update_item('35998002-7e37-443f-ab43-e4ed7517dce3', item_json)

# item =  '{ "id": "35998002-7e37-443f-ab43-e4ed7517dce7", "label":"hello world!", "quantity":1}'
# item_json = json.loads(item)
# create_item(item_json)

print(get_items('SELECT * FROM items'))

delete_item('35998002-7e37-443f-ab43-e4ed7517dce3')

print(get_items('SELECT * FROM items'))