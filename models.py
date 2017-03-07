from chat import db
from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import relationship

class BlogPost(db.Model):
	__tablename__ = "posts"
	
	id =db.Column(db.Integer, primary_key = True)
	posts_id = db.Column(db.Integer, ForeignKey('users.id'))
	username = db.Column(db.String,nullable = False)
	date = db.Column(db.Date, server_default=func.now())
	conversation = db.Column(db.String, nullable=False)
	diagnosis = db.Column(db.String, nullable=True)
	exercises =  db.Column(db.String, nullable=True)
	planning = db.Column(db.String, nullable=True)

	def __init__(self,username, conversation):
		self.username = username
		self.conversation = conversation
	
	
	def __repr__(self):
		return '<{}>'.format(self.conversation)


class UsersTable(db.Model):
	__tablename__ = "userstable"

	user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        
   def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<name - {}>'.format(self.name)