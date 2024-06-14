import sqlite3
import click
from suppliers import add_supplier, update_supplier, list_suppliers, search_suppliers, delete_supplier
from orders import create_order, update_order, list_orders, search_orders, delete_order
from logistics import record_logistics, update_logistics, list_logistics, search_logistics, delete_logistics
from items import add_item, update_item, list_items, search_items, delete_item
from database import initialize_database, get_connection, execute_query_fetchall

DB_FILE = 'liquor_supply.db'

# Function to display welcome message
def display_welcome_message():
    click.echo("""
 _   _      _ _             _____                           
| | | |    | | |           |  __ \\                          
| |_| | ___| | | ___       | |  \\/ ___  ___  _ __ __ _  ___ 
|  _  |/ _ \\ | |/ _ \\      | | __ / _ \\/ _ \\| '__/ _` |/ _ \\
| | | |  __/ | | (_) |  _  | |_\\ \\  __/ (_) | | | (_| |  __/
\\_| |_|\\___|_|_|\\___/  ( )  \\____/\\___|\\___/|_|  \\__, |\\___|
                       |/                         __/ |     
                                                 |___/      

    🍾🍷 Welcome to Liquor Supply Pro -- Your Supply Chain Management Solution 🍺🥃
    """)

# Click command group for CLI
@click.group()
def cli():
    """Liquor Supply Pro CLI"""
    pass

# Helper function to prompt user with dropdown menu
def prompt_with_dropdown(options, prompt_message):
    # Sort options by ID in ascending order
    options.sort(key=lambda x: x[0])
    
    option_names = [f"{option[0]} - {option[1]}" for option in options]
    option_names.append("Cancel")
    
    while True:
        try:
            selected_option = click.prompt(prompt_message, type=click.Choice(option_names, case_sensitive=False))
            
            if selected_option.lower() == "cancel":
                return None
            
            for option in options:
                if f"{option[0]} - {option[1]}" == selected_option:
                    return option[0]
            
            # If no valid option matched
            raise ValueError("Invalid option selected.")
        
        except ValueError as e:
            click.echo(f"Error: {e}. Please select a valid option.")

# Helper function to select a supplier from dropdown
def select_supplier(conn):
    suppliers = execute_query_fetchall(conn, "SELECT id, name FROM suppliers")
    if not suppliers:
        click.echo("No suppliers available. Please add a supplier first.")
        return None
    return prompt_with_dropdown(suppliers, "Select Supplier (ID - Name):")

# Helper function to select an order from dropdown
def select_order(conn):
    orders = execute_query_fetchall(conn, "SELECT id, customer_name FROM orders")
    if not orders:
        click.echo("No orders available. Please create an order first.")
        return None
    return prompt_with_dropdown(orders, "Select Order (ID - Customer Name):")

# Supplier Commands
@cli.group()
def suppliers():
    """Manage Suppliers"""
    pass

@suppliers.command()
@click.option('--name', prompt='Supplier name', help='Name of the supplier.')
@click.option('--contact_name', prompt='Contact name', help='Name of the contact person.')
@click.option('--contact_phone', prompt='Contact phone', help='Contact phone number.')
@click.option('--address', prompt='Address', help='Address of the supplier.')
def add(name, contact_name, contact_phone, address):
    """Add a new supplier"""
    conn = get_connection(DB_FILE)
    add_supplier(conn, name, contact_name, contact_phone, address)
    click.echo(f"Supplier '{name}' added successfully.")

@suppliers.command()
def list():
    """List all suppliers"""
    conn = get_connection(DB_FILE)
    suppliers = execute_query_fetchall(conn, "SELECT id, name FROM suppliers")
    if not suppliers:
        click.echo("No suppliers found.")
    else:
        click.echo("List of Suppliers:")
        for supplier in suppliers:
            click.echo(f"ID: {supplier[0]}, Name: {supplier[1]}")

@suppliers.command()
@click.argument('keyword')
def search(keyword):
    """Search suppliers"""
    conn = get_connection(DB_FILE)
    search_suppliers(conn, keyword)

@suppliers.command()
@click.option('--supplier_id', prompt='Supplier ID', type=int, help='ID of the supplier to update.')
@click.option('--name', prompt='Supplier name', help='Name of the supplier.')
@click.option('--contact_name', prompt='Contact name', help='Name of the contact person.')
@click.option('--contact_phone', prompt='Contact phone', help='Contact phone number.')
@click.option('--address', prompt='Address', help='Address of the supplier.')
def update(supplier_id, name, contact_name, contact_phone, address):
    """Update a supplier"""
    conn = get_connection(DB_FILE)
    update_supplier(conn, supplier_id, name, contact_name, contact_phone, address)
    click.echo(f"Supplier '{name}' updated successfully.")

@suppliers.command()
@click.option('--supplier_id', prompt='Supplier ID', type=int, help='ID of the supplier to delete.')
def delete(supplier_id):
    """Delete a supplier"""
    conn = get_connection(DB_FILE)
    delete_supplier(conn, supplier_id)
    click.echo(f"Supplier with ID '{supplier_id}' deleted successfully.")

# Order Commands
@cli.group()
def orders():
    """Manage Orders"""
    pass

@orders.command()
@click.option('--customer_name', prompt='Customer name', help='Name of the customer.')
@click.option('--order_date', prompt='Order date', help='Date of the order.')
@click.option('--total_amount', prompt='Total amount', type=float, help='Total amount of the order.')
def create(customer_name, order_date, total_amount):
    """Create a new order"""
    conn = get_connection(DB_FILE)
    supplier_id = select_supplier(conn)
    if supplier_id:
        create_order(conn, customer_name, order_date, total_amount, supplier_id)
        click.echo(f"Order for '{customer_name}' created successfully.")

@orders.command()
def list():
    """List all orders"""
    conn = get_connection(DB_FILE)
    orders = execute_query_fetchall(conn, "SELECT id, customer_name FROM orders")
    if not orders:
        click.echo("No orders found.")
    else:
        click.echo("List of Orders:")
        for order in orders:
            click.echo(f"ID: {order[0]}, Customer Name: {order[1]}")

@orders.command()
@click.argument('keyword')
def search(keyword):
    """Search orders"""
    conn = get_connection(DB_FILE)
    search_orders(conn, keyword)

@orders.command()
@click.option('--order_id', prompt='Order ID', type=int, help='ID of the order to update.')
@click.option('--status', prompt='Order status', help='Status of the order.')
def update(order_id, status):
    """Update an order"""
    conn = get_connection(DB_FILE)
    update_order(conn, order_id, status)
    click.echo(f"Order with ID '{order_id}' updated successfully.")

@orders.command()
@click.option('--order_id', prompt='Order ID', type=int, help='ID of the order to delete.')
def delete(order_id):
    """Delete an order"""
    conn = get_connection(DB_FILE)
    delete_order(conn, order_id)
    click.echo(f"Order with ID '{order_id}' deleted successfully.")

# Logistics Commands
@cli.group()
def logistics():
    """Manage Logistics"""
    pass

@logistics.command()
@click.option('--dispatch_date', prompt='Dispatch date', help='Date of dispatch.')
@click.option('--arrival_date', prompt='Arrival date', help='Date of arrival.')
@click.option('--status', prompt='Status', help='Status of the logistics.')
def record(dispatch_date, arrival_date, status):
    """Record logistics details"""
    conn = get_connection(DB_FILE)
    order_id = select_order(conn)
    supplier_id = select_supplier(conn)
    if order_id and supplier_id:
        record_logistics(conn, order_id, supplier_id, dispatch_date, arrival_date, status)
        click.echo("Logistics recorded successfully.")

@logistics.command()
def list():
    """List all logistics entries"""
    conn = get_connection(DB_FILE)
    logistics = execute_query_fetchall(conn, "SELECT id, order_id FROM logistics")
    if not logistics:
        click.echo("No logistics entries found.")
    else:
        click.echo("List of Logistics Entries:")
        for logistic in logistics:
            click.echo(f"ID: {logistic[0]}, Order ID: {logistic[1]}")

@logistics.command()
@click.argument('keyword')
def search(keyword):
    """Search logistics entries"""
    conn = get_connection(DB_FILE)
    search_logistics(conn, keyword)

@logistics.command()
@click.option('--logistics_id', prompt='Logistics ID', type=int, help='ID of the logistics to update.')
@click.option('--status', prompt='Status', help='Status of the logistics.')
def update(logistics_id, status):
    """Update logistics details"""
    conn = get_connection(DB_FILE)
    update_logistics(conn, logistics_id, status)
    click.echo(f"Logisticswith ID '{logistics_id}' updated successfully.")

@logistics.command()
@click.option('--logistics_id', prompt='Logistics ID', type=int, help='ID of the logistics to delete.')
def delete(logistics_id):
    """Delete logistics entry"""
    conn = get_connection(DB_FILE)
    delete_logistics(conn, logistics_id)
    click.echo(f"Logistics with ID '{logistics_id}' deleted successfully.")

# Item Commands
@cli.group()
def items():
    """Manage Items"""
    pass

@items.command()
@click.option('--name', prompt='Item name', help='Name of the item.')
@click.option('--price', prompt='Item price', type=float, help='Price of the item.')
def add(name, price):
    """Add a new item"""
    conn = get_connection(DB_FILE)
    supplier_id = select_supplier(conn)
    if supplier_id:
        add_item(conn, name, price, supplier_id)
        click.echo(f"Item '{name}' added successfully.")

@items.command()
def list():
    """List all items"""
    conn = get_connection(DB_FILE)
    items = execute_query_fetchall(conn, "SELECT id, name FROM items")
    if not items:
        click.echo("No items found.")
    else:
        click.echo("List of Items:")
        for item in items:
            click.echo(f"ID: {item[0]}, Name: {item[1]}")

@items.command()
@click.argument('keyword')
def search(keyword):
    """Search items"""
    conn = get_connection(DB_FILE)
    search_items(conn, keyword)

@items.command()
@click.option('--item_id', prompt='Item ID', type=int, help='ID of the item to update.')
@click.option('--name', prompt='Item name', help='Name of the item.')
@click.option('--price', prompt='Item price', type=float, help='Price of the item.')
def update(item_id, name, price):
    """Update an item"""
    conn = get_connection(DB_FILE)
    supplier_id = select_supplier(conn)
    if supplier_id:
        update_item(conn, item_id, name, price, supplier_id)
        click.echo(f"Item with ID '{item_id}' updated successfully.")

@items.command()
@click.option('--item_id', prompt='Item ID', type=int, help='ID of the item to delete.')
def delete(item_id):
    """Delete an item"""
    conn = get_connection(DB_FILE)
    delete_item(conn, item_id)
    click.echo(f"Item with ID '{item_id}' deleted successfully.")

# Main CLI command group
cli.add_command(suppliers)
cli.add_command(orders)
cli.add_command(logistics)
cli.add_command(items)

# Main block to initialize database and run CLI
if __name__ == '__main__':
    display_welcome_message()  # Display welcome message
    initialize_database(DB_FILE)  # Initialize database schema with the DB_FILE
    try:
        cli()  # Run the CLI
    except sqlite3.Error as e:
        click.echo(f"SQLite error occurred: {e}")
    except Exception as e:
        click.echo(f"Error occurred: {e}")


