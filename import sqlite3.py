import sqlite3
# Create or connect to the database file
conn = sqlite3.connect('restaurant_orders.db')
cursor = conn.cursor()

# Create the 'orders' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        order_id TEXT,
        date TEXT,
        total_amount INTEGER
    )
''')

# Create the 'order_items' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS order_items (
        id INTEGER PRIMARY KEY,
        order_id TEXT,
        item_name TEXT,
        price INTEGER
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()
def insert_order(order_id, date, total_amount, items):
    conn = sqlite3.connect('restaurant_orders.db')
    cursor = conn.cursor()

    # Insert into 'orders' table
    cursor.execute('INSERT INTO orders (order_id, date, total_amount) VALUES (?, ?, ?)',
                   (order_id, date, total_amount))
    
    order_id = cursor.lastrowid  # Get the inserted row's ID

    # Insert order items into 'order_items' table
    for item_name, price in items:
        cursor.execute('INSERT INTO order_items (order_id, item_name, price) VALUES (?, ?, ?)',
                       (order_id, item_name, price))
    
    conn.commit()
    conn.close()

# Usage example:
order_id = ORDER_ID()
date = "2023-08-30"
total_amount = 350
items = [("Fried Calamari", 100), ("Beach Burger", 140)]  # Example list of order items
insert_order(order_id, date, total_amount, items)
def get_order_history():
    conn = sqlite3.connect('restaurant_orders.db')
    cursor = conn.cursor()

    def get_order_history():
    conn = sqlite3.connect('restaurant_orders.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM orders')
    orders = cursor.fetchall()

    for order in orders:
        print("Order ID:", order[1])
        print("Date:", order[2])
        print("Total Amount:", order[3])

        cursor.execute('SELECT item_name, price FROM order_items WHERE order_id = ?', (order[0],))
        order_items = cursor.fetchall()
        
        for item in order_items:
            print("Item:", item[0])
            print("Price:", item[1])
    
    conn.close()

# Usage example:
get_order_history()
