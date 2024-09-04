import sqlite3
from datetime import datetime

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