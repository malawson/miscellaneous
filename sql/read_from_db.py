import sqlite3

prompt = """
Select options [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""

with sqlite3.connect("newnum.db") as connection:
	c = connection.cursor()

	while True:
		x = raw_input(prompt)	

		# Check input
		if x in set(["1", "2", "3", "4"]): 
			operation = {1: "avg", 2: "max", 3: "min", 4: "sum"}[int(x)]

			c.execute("SELECT {}(integers) FROM numbers".format(operation))

			get = c.fetchone()
			print operation + ": %f" % get[0]

		else: 
			print "Exit"
			break
