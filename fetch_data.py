import sqlite3

def view_runs():
    conn = sqlite3.connect('running_app.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM runs")
    rows = cursor.fetchall()

    conn.close()

    for row in rows:
        print(row)

if __name__ == "__main__":
    view_runs()

