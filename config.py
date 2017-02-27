import os
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = "I\xdd\xa21\x8a\xd02\xdd\xe8x\xd8_\xc9\x86\x0c3\x1de\xc3\xcd\x9a\xa7\xc0\x1f"
	SQALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False