
import sqlite3

"""

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	c.execute("UPDATE population SET population = 90000 WHERE city= 'New York City'")
	c.execute("DELETE FROM population WHERE city='Boston'")

	print "\nNEW DATA: \n"
	c.execute("SELECT * FROM population")
	rows = c.fetchall()

	for r in rows:
		print r[0], r[1], r[2]

"""
"""
import sqlite3 

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	cities = [
		('Boston', 'MA', 600000),
		('LA', 'CA', 600000),
		('Houston', 'TX', 600000),
		('Philadelphia', 'PA', 600000),
		('San Antonio', 'TX', 600000),
		('San Diego', 'CA', 600000),
		('Dallas', 'TX', 600000),
		('San Jose', 'CA', 600000),
		('Jacksonville', 'FL', 600000)
		]

	c.executemany("INSERT INTO population VALUES(?, ?, ?)", cities)
	c.execute ("SELECT * FROM population WHERE population > 1000")

	rows = c.fetchall()

	for r in rows:
		print r[0], r[1], r[2]

"""
"""
import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	c.execute("CREATE TABLE regions (city TEXT, region TEXT)")

	cities = [
		('New York City', 'Northeast'),
		('San Francisco', 'West'),
		('Chicago', 'Midwest'),
		('Boston', 'Northeast'),
		('Phoenix', 'West'),
		('LA', 'West'),
		('San Jose', 'West'),
		('San Antonio', 'South'),
		('Dallas', 'South'),
		('Indianapolis', 'Midwest'),
		('Jacksonville', 'South')
		]

	c.executemany("INSERT INTO regions VALUES(?, ?)", cities)
	c.execute("SELECT * FROM regions ORDER BY region ASC")

	rows = c.fetchall()

	for r in rows:
		print r[0], r [1]

"""

# Let's join data from some tables 


import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	c.execute("""SELECT population.city, population.population, regions.region FROM population 
		INNER JOIN regions ON population.city = regions.city ORDER by population.city ASC""")

	rows = c.fetchall()

	for r in rows:
		print "City: " + r[0]
		print "Population: " + str(r[1])
		print "Region: " + r[2]
		print



