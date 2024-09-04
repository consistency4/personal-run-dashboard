#creating the table
import sqlite3
from datetime import datetime

# Function to create the 'runs' table if it doesn't exist
def create_table():
    conn = sqlite3.connect('running_app.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS runs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        distance REAL NOT NULL,
        intensity TEXT NOT NULL,
        notes TEXT
    )
    ''')

    conn.commit()
    conn.close()