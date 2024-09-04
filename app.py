from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import pandas as pd
import plotly.express as px
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv('sk-ommlY0ovwnRDyEuf09eV3PfBiZln2WAqsNLprj8Jf7T3BlbkFJpN_5J4GUhriR1iZjP5rQDk10QSYp-lCKQ1nVEHaxMA')

# Function to create the table if it doesn't exist
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

# Function to get data from the database
def get_run_data():
    conn = sqlite3.connect('running_app.db')
    df = pd.read_sql_query("SELECT * FROM runs", conn)
    conn.close()
    return df

# Route to display the form
@app.route('/input_run')
def input_run():
    return render_template('input_run.html')

# Route to handle the form submission
@app.route('/submit_run', methods=['POST'])
def submit_run():
    # Get form data
    date = request.form['date']
    time = request.form['time']
    distance = request.form['distance']
    intensity = request.form['intensity']
    notes = request.form['notes']

    # Save data to the database
    conn = sqlite3.connect('running_app.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO runs (date, time, distance, intensity, notes)
    VALUES (?, ?, ?, ?, ?)
    ''', (date, time, distance, intensity, notes))

    conn.commit()
    conn.close()

    # Redirect to the dashboard or another page
    return redirect(url_for('dashboard'))

# Route to render the dashboard
@app.route('/')
def dashboard():
    df = get_run_data()

    # Create a Plotly graph
    fig = px.line(df, x='date', y='distance', title='Running Distance Over Time')
    
    # Convert the Plotly figure to HTML
    graph_html = fig.to_html(full_html=False)
    
    return render_template('dashboard.html', graph_html=graph_html)

# Route to render the chat interface
@app.route('/chat')
def chat():
    return render_template('chat.html')

# Route to handle chat interaction
@app.route('/chat_response', methods=['POST'])
def chat_response():
    # Get user message from form
    user_message = request.form['message']

    # Fetch the user's running stats from the database
    df = get_run_data()

    # Create a summary of the user's stats (you can customize this)
    recent_run = df.iloc[-1] if not df.empty else None
    if recent_run is not None:
        user_stats = f"Your last run was {recent_run['distance']} miles at a {recent_run['intensity']} intensity on {recent_run['date']}."
    else:
        user_stats = "You have not logged any runs yet."

    # Create a prompt for OpenAI
    system_message = f"You are an AI coach. Based on the following running stats, recommend what the user should do next: {user_stats}."
    user_message_content = user_message

    # Call OpenAI API to generate a response using the new ChatCompletion API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or use "gpt-4" if available
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message_content}
        ]
    )

    # Extract the AI's response
    ai_message = response['choices'][0]['message']['content'].strip()

    # Render the chat template with the user's message and AI's response
    return render_template('chat.html', user_message=user_message, ai_message=ai_message)

if __name__ == "__main__":
    create_table()  # Ensure the table is created before running the app
    app.run(debug=True)
