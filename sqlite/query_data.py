import sqlite3

#Connect to database
conn = sqlite3.connect('poker.db')

#Create a cursor
c = conn.cursor()

#Query Data
c.execute("SELECT call_amount FROM poker_hands WHERE rowid = 45")
items = c.fetchall()
for item in items:
	print(item)

#Commit command
conn.commit()

#Close connection
conn.close()