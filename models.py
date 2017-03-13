from flask.ext.sqlalchemy import SQLAlchemy
from chat import app

db = SQLAlchemy(app)

from sqlalchemy import func, Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#NoReferrenceColumnError
'''
associations = db.Table('associations',
    db.Column('diag_id', db.Integer, db.ForeignKey('diagnosistable.id')),
    db.Column('exerc_id', db.Integer, db.ForeignKey('exercisestable.id'))
)
'''
db.drop_all()

class UsersTable(db.Model):
	__tablename__ = "userstable"

	id = db.Column('id', db.Integer, primary_key=True)
	name = db.Column('name', db.Unicode,nullable = False)
	email = db.Column('email', db.String, nullable=False)
	password = db.Column('password', db.String)
	posts_id = db.Column('posts_id', db.Integer)#, db.ForeignKey('posts.id'))
	diagnosis_id = db.Column('diagnosis_id', db.Integer)#, db.ForeignKey('diagnosistable.id'))
	exercises_id = db.Column('exercises_id', db.Integer)#, db.ForeignKey('exercisestable.id'))
	'''
	posts = db.relationship('ChatPost', back_populates="user") # One(user)-to-many(posts)
	diagnostic = db.relationship('DiagnosisTable', foreign_keys = diagnosis_id) # One(user)-to-many(diagnosis)
	exercises = db.relationship('ExercisesTable', foreign_keys = exercises_id) # One(user)-to-many(exercises)
	'''

	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = password
	'''	
	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)
	'''

	def __repr__(self):
		return '<name - {}>'.format(self.name)

class ChatPost(db.Model):
	__tablename__ = "posts"

	id =db.Column('id', db.Integer, primary_key = True)
	words_list = db.Column('words_list', db.String)
	diagnosis_id = db.Column('diagnosis_id', db.String)#, db.ForeignKey('diagnosistable.id'), nullable = True)
	user_id = db.Column('user_id', db.String)#, db.ForeignKey('userstable.id'))
	date = db.Column('data', db.Date, server_default=func.now())

	'''
	user = db.relationship('UsersTable', back_populates="posts") # Many(posts)-to-one(user)
	diagnos = db.relationship('DiagnosisTable', foreign_keys = diagnosis_id) # One(post)-to-one(diagnosis)
	'''

	def __init__(self,list_of_words):
		self.words_list = list_of_words
	
	def __repr__(self):
		return '<{}>'.format(self.words_list)


class DiagnosisTable(db.Model):
	__tablename__ = "diagnosistable"

	id = db.Column('id', db.Integer, primary_key = True)
	diagnosis_name = db.Column('diagnosis_name', db.String)
	key_words = db.Column('key_words', db.String)
	#exercises = db.relationship('ExercisesTable', back_populates="diagnosis")

	# Try to debug this part to create a Many-t-many relationship with associations table
	#exercises = db.relationship("ExercisesTable", secondary = associations) #Many(diagnosis)-to-many(exercises)


class ExercisesTable(db.Model):
	__tablename__ = "exercisestable"

	id = db.Column('id', db.Integer, primary_key = True)
	exercises_name = db.Column('exercise_name', db.Unicode)
	planning = db.Column('planning', db.String)
	description = db.Column('description', db.String)
	diagnosis_id = db.Column('diagnosis_id', db.Integer)#, db.ForeignKey('diagnosistable.id'))
	'''
	diagnosis = db.relationship('DiagnosisTable', back_populates="exercises") # Many(exercises)-to-one(diagnosis)
	'''

# create the database and the db tables
db.create_all()
DefaultUser1 = db.session.add(UsersTable("Default_User_Name", "defaultemail@default.org", "basicpassword1"))
db.session.commit()
