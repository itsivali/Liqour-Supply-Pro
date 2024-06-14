import sqlite3

DB_FILE = 'liquor_supply.db'

def initialize_database(db_file):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    
    c.execute("""
    CREATE TABLE IF NOT EXISTS suppliers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        contact_name TEXT,
        contact_phone TEXT,
        address TEXT
    )
    """)

    
    c.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL,
        supplier_id INTEGER,
        FOREIGN KEY (supplier_id) REFERENCES suppliers (id)
    )
    """)

    
    c.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        order_date TEXT,
        total_amount REAL,
        supplier_id INTEGER,
        FOREIGN KEY (supplier_id) REFERENCES suppliers (id)
    )
    """)

   
    c.execute("""
    CREATE TABLE IF NOT EXISTS logistics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER,
        supplier_id INTEGER,
        dispatch_date TEXT,
        arrival_date TEXT,
        status TEXT,
        FOREIGN KEY (order_id) REFERENCES orders (id),
        FOREIGN KEY (supplier_id) REFERENCES suppliers (id)
    )
    """)

    conn.commit()
    conn.close()

def get_connection(db_file):
    return sqlite3.connect(db_file)

def execute_query(conn, query, params=()):
    try:
        c = conn.cursor()
        c.execute(query, params)
        conn.commit()
        return True
    except sqlite3.IntegrityError as e:
        print(f"Integrity Error: {e}")
        return False
    except sqlite3.Error as e:
        print(f"Database Error: {e}")
        return False

def execute_query_fetchall(conn, query, params=()):
    try:
        c = conn.cursor()
        c.execute(query, params)
        rows = c.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Database Error: {e}")
        return []

def execute_query_fetchone(conn, query, params=()):
    try:
        c = conn.cursor()
        c.execute(query, params)
        row = c.fetchone()
        return row
    except sqlite3.Error as e:
        print(f"Database Error: {e}")
        return None

