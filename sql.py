'''
Use for creating a sqlite database and run chat.py locally
To deploy the chat app on heroku the database migrates from sqlite to postgresql
'''

import sqlite3
with sqlite3.connect("localkinebotdb.db") as connection:
	c = connection.cursor()
	c.execute("DROP TABLE posts") # posts is the name of the table, it is meant to be changed
	c.execute("CREATE TABLE posts(title TEXT, description TEXT)")
	c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
	c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')