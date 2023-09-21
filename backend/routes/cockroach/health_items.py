import logging, json
from routes.cockroach.conn import *
from routes.cockroach.utilities import *


def create_item_table() -> None:
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS items (id UUID PRIMARY KEY, label VARCHAR(255), quantity INTEGER, description TEXT, url VARCHAR(255))"
        )
        logging.debug("create_item_table(): status message: %s",
                        cur.statusmessage)
    conn.commit()
    close_conn(conn)


def delete_item_table() -> None:
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("DROP TABLE items")
        logging.debug("delete_item_table(): status message: %s",
                        cur.statusmessage)
    conn.commit()
    close_conn(conn)


def get_item(id: str) -> dict:
    
    # sanitize
    id = add_string(id)

    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(
            f"SELECT * FROM items WHERE id = '{id}'"
        )
        logging.debug("get_item(): status message: %s",
                        cur.statusmessage)

        # assume get_item always returns exactly one entry
        item = cur.fetchone()
    conn.commit()
    close_conn(conn)

    return item


def get_item_by_label(label: str) -> dict:

    # sanitize
    label = add_string(label)

    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(
            f"SELECT * FROM items WHERE label = '{label}'"
        )
        logging.debug("get_item_by_label(): status message: %s",
                        cur.statusmessage)

        # assume get_item_by_label always returns exactly one entry
        item = cur.fetchone()
    conn.commit()
    close_conn(conn)

    return item


def get_items(query: str) -> [str]:
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(query)
        logging.debug("get_items(): status message: %s",
                        cur.statusmessage)
        items = [_dict for _dict in cur.fetchall()]
    conn.commit()
    close_conn(conn)

    return items


def create_item(item: dict) -> dict:

    # sanitize json data
    item['id'] = add_string(item['id'], '\'', '\'')
    item['description'] = add_string(item['description'], '\'', '\'')
    item['label'] = add_string(item['label'], '\'', '\'')
    item['url'] = add_string(item['url'], '\'', '\'')

    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(
            f"INSERT INTO items (id, label, quantity, description, url) VALUES ('{item['id']}', '{item['label']}', {item['quantity']}, '{item['description']}', '{item['url']}')"
        )
        logging.debug("create_item(): status message: %s",
                        cur.statusmessage)
    conn.commit()
    close_conn(conn)

    # assume create item will always create one entry
    return item


def update_item(item: dict) -> dict:

    # sanitize json data
    item['id'] = add_string(item['id'], '\'', '\'')
    item['description'] = add_string(item['description'], '\'', '\'')
    item['label'] = add_string(item['label'], '\'', '\'')
    item['url'] = add_string(item['url'], '\'', '\'')

    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(
            f"UPDATE items SET label = '{item['label']}', quantity = {item['quantity']}, description = '{item['description']}', url = '{item['url']}' WHERE id = '{item['id']}'"
        )
        logging.debug("update_item(): status message: %s",
                        cur.statusmessage)
    conn.commit()
    close_conn(conn)

    # assume update_item will always update one entry
    return item


def delete_item(id: str) -> bool:

    # sanitize
    id = add_string(id)

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

# delete_item_table()
# create_item_table()

# item =  '{ "id": "35998002-7e37-443f-ab43-e4ed7517dce3", "label":"hello hello!", "quantity":1, "description": "test"}'
# item_json = json.loads(item)
# create_item(item_json)

# print(get_items('SELECT * FROM items'))
# print(get_item('35998002-7e37-443f-ab43-e4ed7517dce3'))

# item =  '{ "id": "35998002-7e37-443f-ab43-e4ed7517dce3", "label":"asasas", "quantity":222, "description": "helloaaa"}'
# item_json = json.loads(item)
# update_item('35998002-7e37-443f-ab43-e4ed7517dce3', item_json)

# # item =  '{ "id": "35998002-7e37-443f-ab43-e4ed7517dce7", "label":"hello world!", "quantity":1}'
# # item_json = json.loads(item)
# # create_item(item_json)

# print(get_items('SELECT * FROM items'))

# delete_item('35998002-7e37-443f-ab43-e4ed7517dce3')

# print(get_items('SELECT * FROM items'))

# create_item_table()

# item =  '{ "id": "35998002-7e37-443f-ab43-e4ed7517dce3", "label":"hello hello!", "quantity":1, "description": "test", "url": "google.com"}'
# item_json = json.loads(item)
# create_item(item_json)
# print(get_items('SELECT * FROM items'))

# print("Yazan")
# [print(item['id'] + ' ' + item['label']) for item in get_items("SELECT * FROM items")]
