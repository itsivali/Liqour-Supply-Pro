import pytest
import sqlite3
from suppliers import add_supplier, update_supplier, list_suppliers, search_suppliers, delete_supplier
from orders import create_order, update_order, list_orders, search_orders, delete_order
from logistics import record_logistics, update_logistics, list_logistics, search_logistics, delete_logistics
from items import add_item, update_item, list_items, search_items, delete_item
from database import initialize_database, get_connection

DB_FILE = ':memory:'

@pytest.fixture
def conn():
    """Fixture to create a new database connection for each test."""
    conn = get_connection(DB_FILE)
    initialize_database(conn)
    yield conn
    conn.close()

# Supplier Tests
def test_add_supplier(conn):
    add_supplier(conn, "ABC Liquors", "John Doe", "123-456-7890", "123 Main Street")
    suppliers = list_suppliers(conn)
    assert len(suppliers) == 1
    assert suppliers[0][1] == "ABC Liquors"

def test_update_supplier(conn):
    add_supplier(conn, "ABC Liquors", "John Doe", "123-456-7890", "123 Main Street")
    supplier_id = list_suppliers(conn)[0][0]
    update_supplier(conn, supplier_id, "XYZ Distributors", "Jane Smith", "987-654-3210", "456 Elm Street")
    suppliers = list_suppliers(conn)
    assert suppliers[0][1] == "XYZ Distributors"

def test_delete_supplier(conn):
    add_supplier(conn, "ABC Liquors", "John Doe", "123-456-7890", "123 Main Street")
    supplier_id = list_suppliers(conn)[0][0]
    delete_supplier(conn, supplier_id)
    suppliers = list_suppliers(conn)
    assert len(suppliers) == 0

def test_search_supplier(conn):
    add_supplier(conn, "ABC Liquors", "John Doe", "123-456-7890", "123 Main Street")
    suppliers = search_suppliers(conn, "ABC")
    assert len(suppliers) == 1
    assert suppliers[0][1] == "ABC Liquors"

# Order Tests
def test_create_order(conn):
    add_supplier(conn, "ABC Liquors", "John Doe", "123-456-7890", "123 Main Street")
    supplier_id = list_suppliers(conn)[0][0]
    create_order(conn, "XYZ Bar & Grill", "2024-06-15", 500.00, supplier_id)
    orders = list_orders(conn)
    assert len(orders) == 1
    assert orders[0][1] == "XYZ Bar & Grill"

def test_update_order(conn):
    add_supplier(conn, "ABC Liquors", "John Doe", "123-456-7890", "123 Main Street")
    supplier_id = list_suppliers(conn)[0][0]
    create_order(conn, "XYZ Bar & Grill", "2024-06-15", 500.00, supplier_id)
    order_id = list_orders(conn)[0][0]
    update_order(conn, order_id, "Completed")
    orders = list_orders(conn)
    assert orders[0][2] == "Completed"

def test_delete_order(conn):
    add_supplier(conn, "ABC Liquors", "John Doe", "123-456-7890", "123 Main Street")
    supplier_id = list_suppliers(conn)[0][0]
    create_order(conn, "XYZ Bar & Grill", "2024-06-15", 500.00, supplier_id)
    order_id = list_orders(conn)[0][0]
    delete_order(conn, order_id)
    orders = list_orders(conn)
    assert len(orders) == 0

def test_search_order(conn):
    add_supplier(conn, "ABC Liquors", "John Doe", "123-456-7890", "123 Main Street")
    supplier_id = list_suppliers(conn)[0][0]
    create_order(conn, "XYZ Bar & Grill", "2024-06-15", 500.00, supplier_id)
    orders = search_orders(conn, "XYZ")
    assert len(orders) == 1
    assert orders[0][1] == "XYZ Bar & Grill"

# Logistics Tests
def test_record_logistics(conn):
    add_supplier(conn, "ABC Liquors", "John Doe", "123-456-7890", "123 Main Street")
    supplier_id = list_suppliers(conn)[0][0]
    create_order(conn, "XYZ Bar & Grill", "2024-06-15", 500.00, supplier_id)
    order_id = list_orders(conn)[0][0]
    record_logistics(conn, order_id, supplier_id, "2024-06-16", "2024-06-18", "In transit")
    logistics = list_logistics(conn)
    assert len(logistics) == 1
    assert logistics[0][3] == "In transit"

def test_update_logistics(conn):
    add_supplier(conn, "ABC Liquors", "John Doe", "123-456-7890", "123 Main Street")
    supplier_id = list_suppliers(conn)[0][0]
    create_order(conn, "XYZ Bar & Grill", "2024-06-15", 500.00, supplier_id)
    order_id = list_orders(conn)[0][0]
    record_logistics(conn, order_id, supplier_id, "2024-06-16", "2024-06-18", "In transit")
    logistics_id = list_logistics(conn)[0][0]
    update_logistics(conn, logistics_id, "Delivered")
    logistics = list_logistics(conn)
    assert logistics[0][3] == "Delivered"

def test_delete_logistics(conn):
    add_supplier(conn, "ABC Liquors", "John Doe", "123-456-7890", "123 Main Street")
    supplier_id = list_suppliers(conn)[0][0]
    create_order(conn, "XYZ Bar & Grill", "2024-06-15", 500.00, supplier_id)
    order_id = list_orders(conn)[0][0]
    record_logistics(conn, order_id, supplier_id, "2024-06-16", "2024-06-18", "In transit")
    logistics_id = list_logistics(conn)[0][0]
    delete_logistics(conn, logistics_id)
    logistics = list_logistics(conn)
    assert len(logistics) == 0

def test_search_logistics(conn):
    add_supplier(conn, "ABC Liquors", "John Doe", "123-456-7890", "123 Main Street")
    supplier_id = list_suppliers(conn)[0][0]
    create_order(conn, "XYZ Bar & Grill", "2024-06-15", 500.00, supplier_id)
    order_id = list_orders(conn)[0][0]
    record_logistics(conn, order_id, supplier_id, "2024-06-16", "2024-06-18", "In transit")
    logistics = search_logistics(conn, "transit")
    assert len(logistics) == 1
    assert logistics[0][3] == "In transit"

# Item Tests
def test_add_item(conn):
    add_supplier(conn, "ABC Liquors", "John Doe", "123-456-7890", "123 Main Street")
    supplier_id = list_suppliers(conn)[0][0]
    add_item(conn, "Whiskey", 50.00, supplier_id)
    items = list_items(conn)
    assert len(items) == 1
    assert items[0][1] == "Whiskey"

def test_update_item(conn):
    add_supplier(conn, "ABC Liquors", "John Doe", "123-456-7890", "123 Main Street")
    supplier_id = list_suppliers(conn)[0][0]
    add_item(conn, "Whiskey", 50.00, supplier_id)
    item_id = list_items(conn)[0][0]
    update_item(conn, item_id, "Premium Whiskey", 60.00, supplier_id)
    items = list_items(conn)
    assert items[0][1] == "Premium Whiskey"
    assert items[0][2] == 60.00

def test_delete_item(conn):
    add_supplier(conn, "ABC Liquors", "John Doe", "123-456-7890", "123 Main Street")
    supplier_id = list_suppliers(conn)[0][0]
    add_item(conn, "Whiskey", 50.00, supplier_id)
    item_id = list_items(conn)[0][0]
    delete_item(conn, item_id)
    items = list_items(conn)
    assert len(items) == 0

def test_search_item(conn):
    add_supplier(conn, "ABC Liquors", "John Doe", "123-456-7890", "123 Main Street")
    supplier_id = list_suppliers(conn)[0][0]
    add_item(conn, "Whiskey", 50.00, supplier_id)
    items = search_items(conn, "Whiskey")
    assert len(items) == 1
    assert items[0][1] == "Whiskey"

