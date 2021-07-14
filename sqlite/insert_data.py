import sqlite3
import Game_Logs as GL


# def add_data():
# Connect to database
conn = sqlite3.connect('poker.db')

# Create a cursor
c = conn.cursor()

data = GL.data

# Insert Data
c.executemany("INSERT INTO poker_hands VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data)

# Commit command
conn.commit()

# Close connection
conn.close()
