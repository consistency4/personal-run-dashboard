import pandas as pd
import datetime
import matplotlib.pyplot as plt 

# Load the CSV file
url_path = "C:\\Users\\Spencer Tate\\OneDrive\\Runningapp\\Backend\\main.py\\runningapp - Sheet1.csv"
df = pd.read_csv(url_path)

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Format the 'Date' column
df['Formatted Date'] = df['Date'].dt.strftime('%a, %b %d')

# Count occurrences of 'easy' in the 'Effort' column
count = df['Effort'].str.contains('easy', case=False, regex=True).sum()
print("Total occurrences of easy efforts:", count)

# Plot the data
plt.figure(figsize=(18, 6))
plt.plot(df['Formatted Date'], df['Distance'], marker='o')

# Annotate each point with its Distance value
for i in range(len(df)):
    plt.annotate(df['Distance'][i], (df['Formatted Date'][i], df['Distance'][i]), 
                 textcoords="offset points", xytext=(0,10), ha='center')

# Add title and labels
plt.title('Running over the past week')
plt.xlabel('Date')
plt.ylabel('Miles')

# Display the plot
plt.show()
