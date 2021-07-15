import sqlite3

#Connect to database
conn = sqlite3.connect('poker.db')

#Create a cursor
c = conn.cursor()

#Create a Table
c.execute("""
	CREATE TABLE poker_hands (
	screenshot text,
	hole_cards text,
	betting_round int,
	com_cards text,
	self_index int,
	position text,
	pot_odds real,
	equity real,
	hand_number int,
	action text,
	raise_amount real,
	call_amount real,
	chips real,
	pot real
)""")

#Commit command
conn.commit()

#Close connection
conn.close()