import sqlite3
import pandas as pd

try:
    # Connect to lesson.db
    conn = sqlite3.connect("../db/lesson.db")
    
    # Read data into DataFrame
    df = pd.read_sql("""
        SELECT li.line_item_id, li.quantity, li.product_id,
               p.product_name, p.price
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id
    """, conn)
    
    # Add total column
    df['total'] = df['quantity'] * df['price']
    
    # Group by product_id
    summary = df.groupby('product_id').agg({
        'line_item_id': 'count',
        'total': 'sum',
        'product_name': 'first'
    }).sort_values('product_name')
    
    print(summary.head())
    
    # Save CSV
    summary.to_csv("assignment8/order_summary.csv", index=False)
    print("CSV file 'order_summary.csv' created.")
    
except Exception as e:
    print("Error:", e)
finally:
    if 'conn' in locals():
        conn.close()

