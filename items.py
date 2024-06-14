from database import execute_query, execute_query_fetchall

def add_item(conn, name, price, supplier_id):
    """Add a new item"""
    query = "INSERT INTO items (name, price, supplier_id) VALUES (?, ?, ?)"
    params = (name, price, supplier_id)
    if execute_query(conn, query, params):
        print("Item added successfully.")
    else:
        print("Failed to add item.")

def update_item(conn, item_id, name, price, supplier_id):
    """Update an item"""
    query = "UPDATE items SET name = ?, price = ?, supplier_id = ? WHERE id = ?"
    params = (name, price, supplier_id, item_id)
    if execute_query(conn, query, params):
        print(f"Item with ID '{item_id}' updated successfully.")
    else:
        print(f"Failed to update item with ID '{item_id}'.")

def list_items(conn):
    """List all items"""
    query = "SELECT * FROM items"
    items = execute_query_fetchall(conn, query)
    for item in items:
        print(item)

def search_items(conn, keyword):
    """Search items by keyword"""
    query = "SELECT * FROM items WHERE name LIKE ?"
    params = (f"%{keyword}%",)
    items = execute_query_fetchall(conn, query, params)
    for item in items:
        print(item)

def delete_item(conn, item_id):
    """Delete an item"""
    query = "DELETE FROM items WHERE id = ?"
    params = (item_id,)
    if execute_query(conn, query, params):
        print(f"Item with ID '{item_id}' deleted successfully.")
    else:
        print(f"Failed to delete item with ID '{item_id}'.")

