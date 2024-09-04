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

# Functions for user input
def get_time_input():
    time_input = input("Please enter the time it took to complete your run (HH:MM:SS): ")
    return datetime.strptime(time_input, "%H:%M:%S").time()

def get_distance():
    return float(input("How many miles did you run? "))

def get_date_input():
    date_input = input("What is today's date? (YYYY-MM-DD): ")
    return datetime.strptime(date_input, "%Y-%m-%d").date()

def get_intensity():
    return input("What was the intensity: easy, medium, hard? ")

def get_notes():
    return input("Please add any additional notes that you would like to mention: ")

# Main function
def main():
    # Ensure the table exists
    create_table()

    # Gather run data
    date = get_date_input()
    time = get_time_input()
    distance = get_distance()
    intensity = get_intensity()
    notes = get_notes()

    # Save run data to database
    save_run_to_db(date, time, distance, intensity, notes)
    
    print("Run data saved successfully!")

if __name__ == "__main__":
    main()

# Function to save run data to the SQLite database
def save_run_to_db(date, time, distance, intensity, notes):
    conn = sqlite3.connect('running_app.db')
    cursor = conn.cursor()

    # Convert date and time to strings
    date_str = date.strftime('%Y-%m-%d')
    time_str = time.strftime('%H:%M:%S')

    cursor.execute('''
    INSERT INTO runs (date, time, distance, intensity, notes)
    VALUES (?, ?, ?, ?, ?)
    ''', (date_str, time_str, distance, intensity, notes))

    conn.commit()
    conn.close()
