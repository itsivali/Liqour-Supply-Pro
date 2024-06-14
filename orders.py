from database import execute_query, execute_query_fetchall

def create_order(conn, customer_name, order_date, total_amount, supplier_id):
    """Create a new order"""
    query = "INSERT INTO orders (customer_name, order_date, total_amount, supplier_id) VALUES (?, ?, ?, ?)"
    params = (customer_name, order_date, total_amount, supplier_id)
    if execute_query(conn, query, params):
        print("Order created successfully.")
    else:
        print("Failed to create order.")

def update_order(conn, order_id, status):
    """Update an order"""
    query = "UPDATE orders SET status = ? WHERE id = ?"
    params = (status, order_id)
    if execute_query(conn, query, params):
        print("Order updated successfully.")
    else:
        print("Failed to update order.")

def list_orders(conn):
    """List all orders"""
    query = "SELECT * FROM orders"
    orders = execute_query_fetchall(conn, query)
    for order in orders:
        print(order)

def search_orders(conn, keyword):
    """Search orders by keyword"""
    query = "SELECT * FROM orders WHERE customer_name LIKE ?"
    params = (f"%{keyword}%",)
    orders = execute_query_fetchall(conn, query, params)
    for order in orders:
        print(order)

def delete_order(conn, order_id):
    """Delete an order"""
    query = "DELETE FROM orders WHERE id = ?"
    params = (order_id,)
    if execute_query(conn, query, params):
        print("Order deleted successfully.")
    else:
        print("Failed to delete order.")

