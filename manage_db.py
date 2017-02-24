# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:55:18 2017
"""
import os
from peewee import *

db_proxy = Proxy()

default_users = [
    {'username': 'default_user', 'date': '2017-02-24','conversation':'default sentence','diagnosis':'healthy'},
]
class DiagnosisModel(Model):
	username = CharField(max_length=20, unique=True)
	date = DateField()
	conversation = TextField()
	diagnosis = CharField(max_length=200)

class Meta:
    database = db_proxy

def add_users():
    for u in default_users:
        try:
            DiagnosisModel.create(username=u['username'],
                          date=u['date'],
						  conversation=u['conversation'],
						  diagnosis=u['diagnosis'])
        except IntegrityError:
            existing_user = DiagnosisModel.get(username=u['username'])
            existing_user.date = u['date']
            existing_user.conversation = u['conversation']
            existing_user.diagnosis = u['diagnosis']
            existing_user.save() 

def retrieve_all():
    results = []
    for u in DiagnosisModel.select().order_by(DiagnosisModel.username):
        results.append(u)
    return results
	
# Import modules based on the environment.
# The HEROKU value first needs to be set on Heroku
# either through the web front-end or through the command
# line (if you have Heroku Toolbelt installed, type the following:
# heroku config:set HEROKU=1).
	
if 'HEROKU' in os.environ:
    import urlparse, psycopg2
    urlparse.uses_netloc.append('postgres')
    url = urlparse.urlparse(os.environ["DATABASE_URL"])
    db = PostgresqlDatabase(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
    db_proxy.initialize(db)
else:
    db = SqliteDatabase('kinebot_localSQLite.db')
    db_proxy.initialize(db)

if __name__ == '__main__':
    db_proxy.connect()
    db_proxy.create_tables([DiagnosisModel], safe=True)
    add_users()
    retrieved_users = retrieve_all()
    for u in retrieved_users:
        print(u.username)
