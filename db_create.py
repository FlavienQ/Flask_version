'''
A simple scipt to create the database through models.py
'''

from chat import db
from models import BlogPost

# create the database and the db tables
db.create_all()

#insert
db.session.add(BlogPost("DefaultUser1","This is a standard conversation."))
db.session.add(BlogPost("DefaultUser2","It will be used to diagnose."))

# commit the changes
db.session.commit()
