from database import execute_query, execute_query_fetchall

def add_supplier(conn, name, contact_name, contact_phone, address):
    """Add a new supplier"""
    query = "INSERT INTO suppliers (name, contact_name, contact_phone, address) VALUES (?, ?, ?, ?)"
    params = (name, contact_name, contact_phone, address)
    if execute_query(conn, query, params):
        print("Supplier added successfully.")
    else:
        print("Failed to add supplier.")

def update_supplier(conn, supplier_id, name, contact_name, contact_phone, address):
    """Update a supplier"""
    query = "UPDATE suppliers SET name = ?, contact_name = ?, contact_phone = ?, address = ? WHERE id = ?"
    params = (name, contact_name, contact_phone, address, supplier_id)
    if execute_query(conn, query, params):
        print("Supplier updated successfully.")
    else:
        print("Failed to update supplier.")

def list_suppliers(conn):
    """List all suppliers"""
    query = "SELECT * FROM suppliers"
    suppliers = execute_query_fetchall(conn, query)
    for supplier in suppliers:
        print(supplier)

def search_suppliers(conn, keyword):
    """Search suppliers by keyword"""
    query = "SELECT * FROM suppliers WHERE name LIKE ? OR contact_name LIKE ?"
    params = (f"%{keyword}%", f"%{keyword}%")
    suppliers = execute_query_fetchall(conn, query, params)
    for supplier in suppliers:
        print(supplier)

def delete_supplier(conn, supplier_id):
    """Delete a supplier"""
    query = "DELETE FROM suppliers WHERE id = ?"
    params = (supplier_id,)
    if execute_query(conn, query, params):
        print("Supplier deleted successfully.")
    else:
        print("Failed to delete supplier.")

