'''
This scirpt does not work

'''
import os
import redis
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from chat import app, db

if os.environ['REDIS_URL'] is None:
	redisco.connection_setup(host='localhost', port=5432)
	DATABASE_URL='postgres://localkinebotdb'

app.config.from_object(os.environ['APP_SETTINGS'])
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
	manager.run()