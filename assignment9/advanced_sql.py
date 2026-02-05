import sqlite3

DB_PATH = "../db/lesson.db"

with sqlite3.connect(DB_PATH) as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    print("Connected successfully")

    # Task 1: Complex JOINs with Aggregation
   
    print("\nTASK 1: Total price of first 5 orders")

    cursor.execute("""
        SELECT
            o.order_id,
            SUM(li.quantity * p.price) AS total_price
        FROM orders o
        JOIN line_items li ON o.order_id = li.order_id
        JOIN products p ON li.product_id = p.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id
        LIMIT 5;
    """)

    for row in cursor.fetchall():
        print(row)

   
    # Task 2: Subquery – Average order price per customer

    print("\nTASK 2: Average order price per customer")

    cursor.execute("""
        SELECT
            c.customer_name,
            AVG(sub.total_price) AS average_total_price
        FROM customers c
        LEFT JOIN (
            SELECT
                o.customer_id AS customer_id_b,
                SUM(li.quantity * p.price) AS total_price
            FROM orders o
            JOIN line_items li ON o.order_id = li.order_id
            JOIN products p ON li.product_id = p.product_id
            GROUP BY o.order_id
        ) sub
        ON c.customer_id = sub.customer_id_b
        GROUP BY c.customer_id
        ORDER BY c.customer_name;
    """)

    for row in cursor.fetchall():
        print(row)

   
    # Task 3: Insert Transaction Based on Data
    
    print("\nTASK 3: Create new order and line items")

    
    cursor.execute(
        "SELECT customer_id FROM customers WHERE customer_name = ?;",
        ("Perez and Sons",)
    )
    customer_id = cursor.fetchone()[0]

    
    cursor.execute("""
        SELECT employee_id
        FROM employees
        WHERE first_name = ? AND last_name = ?;
    """, ("Miranda", "Harris"))
    employee_id = cursor.fetchone()[0]

  
    cursor.execute("""
        SELECT product_id
        FROM products
        ORDER BY price ASC
        LIMIT 5;
    """)
    product_ids = [row[0] for row in cursor.fetchall()]

    try:
        cursor.execute("BEGIN;")

        cursor.execute("""
        INSERT INTO orders (customer_id, employee_id, date)
        VALUES (?, ?, DATE('now'))
        RETURNING order_id;
        """, (customer_id, employee_id))


      
       


        new_order_id = cursor.fetchone()[0]

        for pid in product_ids:
            cursor.execute("""
                INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, ?);
            """, (new_order_id, pid, 10))

        cursor.execute("COMMIT;")

    except Exception as e:
        cursor.execute("ROLLBACK;")
        raise e

    cursor.execute("""
        SELECT
            li.line_item_id,
            li.quantity,
            p.product_name
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id
        WHERE li.order_id = ?
        ORDER BY li.line_item_id;
    """, (new_order_id,))

    print(f"New order_id: {new_order_id}")
    for row in cursor.fetchall():
        print(row)

    # Task 4

    print("\nTASK 4: Employees with more than 5 orders")

    cursor.execute("""
        SELECT
            e.employee_id,
            e.first_name,
            e.last_name,
            COUNT(o.order_id) AS order_count
        FROM employees e
        JOIN orders o ON e.employee_id = o.employee_id
        GROUP BY e.employee_id
        HAVING COUNT(o.order_id) > 5
        ORDER BY order_count DESC;
    """)

    for row in cursor.fetchall():
        print(row)
