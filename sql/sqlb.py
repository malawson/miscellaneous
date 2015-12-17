import sqlite3


conn = sqlite3.connect("new.db")

cursor = conn.cursor()

try:
	cursor.execute("INSERT INTO populations VALUES ('Djibouti', 'Djibouti', 11111)")
	conn.commit()
except sqlite3.OperationalError as e:
	print "Oops! something broke:", e.args, " please try again..." 
conn.close()






"""
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	# insert multiple records as list of tuples

	cities = [
			('Boston', 'MA', 2939432),
			('Manchester', 'UK', 345535),
			('Gotham', 'Pluto', 96099)
			]

	c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)

#################

"""
"""
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	c.execute(" INSERT INTO population VALUES('London', 'UK', 0000)")
"""



"""
conn = sqlite3.connect("new.db")
cursor = conn.cursor()

cursor.execute(" INSERT INTO population VALUES ('New York City', 'NY', 11111)")

cursor.execute(" INSERT INTO population VALUES ('San Francisco', 'CA', 22222)")

conn.commit()

conn.close()
"""