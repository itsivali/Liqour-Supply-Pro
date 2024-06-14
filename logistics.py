from database import execute_query, execute_query_fetchall

def record_logistics(conn, order_id, supplier_id, dispatch_date, arrival_date, status):
    """Record logistics details"""
    query = "INSERT INTO logistics (order_id, supplier_id, dispatch_date, arrival_date, status) VALUES (?, ?, ?, ?, ?)"
    params = (order_id, supplier_id, dispatch_date, arrival_date, status)
    if execute_query(conn, query, params):
        print("Logistics recorded successfully.")
    else:
        print("Failed to record logistics.")

def update_logistics(conn, logistics_id, status):
    """Update logistics details"""
    query = "UPDATE logistics SET status = ? WHERE id = ?"
    params = (status, logistics_id)
    if execute_query(conn, query, params):
        print("Logistics updated successfully.")
    else:
        print("Failed to update logistics.")

def list_logistics(conn):
    """List all logistics entries"""
    query = "SELECT * FROM logistics"
    logistics_entries = execute_query_fetchall(conn, query)
    for entry in logistics_entries:
        print(entry)

def search_logistics(conn, keyword):
    """Search logistics entries by keyword"""
    query = "SELECT * FROM logistics WHERE status LIKE ?"
    params = (f"%{keyword}%",)
    logistics_entries = execute_query_fetchall(conn, query, params)
    for entry in logistics_entries:
        print(entry)

def delete_logistics(conn, logistics_id):
    """Delete logistics entry"""
    query = "DELETE FROM logistics WHERE id = ?"
    params = (logistics_id,)
    if execute_query(conn, query, params):
        print("Logistics entry deleted successfully.")
    else:
        print("Failed to delete logistics entry.")

