
import sqlite3
import random 

with sqlite3.connect("newnum.db") as connection:
	c = connection.cursor()

	c.execute(""" DROP TABLE if exists numbers """)
	c.execute(""" CREATE TABLE numbers (integers INT) """)

	for i in range(100):
		c.execute(""" INSERT INTO numbers (integers) VALUES (?) """, (random.randint(0, 100),))

		
	c.execute(""" SELECT numbers.integers FROM numbers """)
	rows = c.fetchall()
	for r in rows:
		print r[0]