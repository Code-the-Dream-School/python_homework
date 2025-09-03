import sqlite3
import csv

try:
    # --- Connect to magazines database ---
    conn = sqlite3.connect("../db/magazines.db")
    cursor = conn.cursor()
    print("Database connected successfully.")

    # --- Drop existing tables (fresh start) ---
    cursor.execute("DROP TABLE IF EXISTS subscriptions")
    cursor.execute("DROP TABLE IF EXISTS subscribers")
    cursor.execute("DROP TABLE IF EXISTS magazines")
    cursor.execute("DROP TABLE IF EXISTS publishers")

    # --- Create tables ---
    cursor.execute("""
    CREATE TABLE publishers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE magazines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT UNIQUE NOT NULL,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id) REFERENCES publishers(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE subscribers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT NOT NULL,
        UNIQUE(name, address)
    )
    """)

    cursor.execute("""
    CREATE TABLE subscriptions (
        subscriber_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        expiration_date TEXT NOT NULL,
        PRIMARY KEY (subscriber_id, magazine_id),
        FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
        FOREIGN KEY (magazine_id) REFERENCES magazines(id)
    )
    """)

    conn.commit()
    print("Tables created successfully.")

    # --- Insert sample data ---
    publishers = ["Tech Monthly", "Health Today", "Adventure Weekly"]
    for pub in publishers:
        cursor.execute("INSERT OR IGNORE INTO publishers (name) VALUES (?)", (pub,))

    magazines = [
        ("AI Insights", 1),
        ("Healthy Living", 2),
        ("Adventure Trips", 3)
    ]
    for title, pub_id in magazines:
        cursor.execute("INSERT OR IGNORE INTO magazines (title, publisher_id) VALUES (?, ?)", (title, pub_id))

    subscribers = [
        ("Alice Johnson", "123 Maple St"),
        ("Bob Smith", "456 Oak St"),
        ("Carol Lee", "789 Pine St")
    ]
    for name, addr in subscribers:
        cursor.execute("INSERT OR IGNORE INTO subscribers (name, address) VALUES (?, ?)", (name, addr))

    subscriptions = [
        (1, 1, "2025-12-31"),
        (2, 2, "2025-11-30"),
        (3, 3, "2025-10-31")
    ]
    for sub_id, mag_id, exp in subscriptions:
        cursor.execute("""
            INSERT OR IGNORE INTO subscriptions (subscriber_id, magazine_id, expiration_date)
            VALUES (?, ?, ?)
        """, (sub_id, mag_id, exp))

    conn.commit()
    print("Sample data inserted successfully.")

    # --- Queries ---
    print("\n--- All Subscribers ---")
    for row in cursor.execute("SELECT * FROM subscribers"):
        print(row)

    print("\n--- All Magazines Sorted by Name ---")
    for row in cursor.execute("SELECT * FROM magazines ORDER BY title"):
        print(row)

    print("\n--- Magazines by Publisher 'Tech Monthly' ---")
    cursor.execute("""
        SELECT m.title, p.name 
        FROM magazines m
        JOIN publishers p ON m.publisher_id = p.id
        WHERE p.name = 'Tech Monthly'
    """)
    for row in cursor.fetchall():
        print(row)

    # --- Export to CSV for assignment submission ---
    cursor.execute("SELECT * FROM subscribers")
    with open("subscribers.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([i[0] for i in cursor.description])  # header
        writer.writerows(cursor.fetchall())

    cursor.execute("SELECT * FROM magazines")
    with open("magazines.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([i[0] for i in cursor.description])  # header
        writer.writerows(cursor.fetchall())

    print("\nCSV files 'subscribers.csv' and 'magazines.csv' created.")

except Exception as e:
    print("Error:", e)

finally:
    if 'conn' in locals():
        conn.close()
        print("Database connection closed.")



