# Liquor Store Pro - Command Line SCM System for Liquor Stores

Liquor Store Pro is a command-line interface (CLI) application designed to streamline Supply Chain Management (SCM) for liquor stores. It facilitates efficient management of inventory, orders, suppliers, and logistics using an SQLite database for data storage and management.

---

## Features

### Inventory Management

#### Add Items

Add new items to the inventory with details such as name, price, and supplier.

```bash
python cli.py items add
Item name: Whiskey
Price: 50.00
Select Supplier (ID - Name):
1 - ABC Liquors
2 - XYZ Distributors
3 - Cancel
Supplier ID: 1
```
## View Inventory

Display current stock levels of all items in the inventory.

```bash
python cli.py inventory view
```
## Update Items
Modify the details of existing items, including price and supplier information.
```bash
python cli.py items update
Item ID: 1
New item name: Premium Whiskey
New price: 60.00
Supplier ID: 1
```
## Remove Items
Delete items from the inventory when they are no longer available.
```bash
python cli.py items delete
Item ID: 1

```
### Order Management
## Customer Orders
Process customer orders, track order status, and manage delivery schedules
```bash
python cli.py orders process
```

## Purchase Orders
Create and manage purchase orders to replenish stock from suppliers.
```bash
python cli.py orders create_purchase
```
## View Inventory

Display current stock levels of all items in the inventory.

```bash
python cli.py inventory view
```
### Items Management
## Update Items
Modify the details of existing items, including price and supplier information.
```bash
python cli.py items update
Item ID: 1
New item name: Premium Whiskey
New price: 60.00
Supplier ID: 1
```

## Remove Items
Delete items from the inventory when they are no longer available.
```bash
python cli.py items delete
Item ID: 1
```

### Order Management
## Customer Orders
Process customer orders, track order status, and manage delivery schedules.
```bash
$ python cli.py orders process
Customer name: XYZ Bar & Grill
Order date: 2024-06-15
Total amount: 500.00
Select Supplier (ID - Name):
1 - ABC Liquors
2 - XYZ Distributors
3 - Cancel
Supplier ID: 1
```
### Purchase Orders
Create and manage purchase orders to replenish stock from suppliers.
```bash
python cli.py orders create_purchase
Supplier name: ABC Liquors
Contact name: John Doe
Contact phone: 123-456-7890
Address: 123 Main Street
Item name: Whiskey
Quantity: 100
```
## Supplier Management

### Supplier Information

Maintain records of suppliers, including contact details and performance metrics.

#### Add Supplier

Add a new supplier to the system with contact information.

```bash
$ python cli.py suppliers add
Supplier name: ABC Liquors
Contact name: John Doe
Contact phone: 123-456-7890
Address: 123 Main Street
```
## View Suppliers
Display a list of all registered suppliers and their details
```bash
python cli.py suppliers view
```
## Update Supplier
Modify the details of an existing supplier.
```bash
python cli.py suppliers update
Supplier ID: 1
New supplier name: XYZ Distributors
New contact name: Jane Smith
New contact phone: 987-654-3210
New address: 456 Elm Street
```
## Remove Supplier
Delete a supplier from the system.
```bash
python cli.py suppliers delete
Supplier ID: 1
```
