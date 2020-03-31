
''' Application configuration file. '''
import os


class Dev(object):
	APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
	SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:donthack@localhost:5432/chena'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	DEBUG=True
	SECRET_KEY = '@#$&*#*@&VVDYhdd)#*83#0(/ckk*'
	# WTF_CSRF_ENABLED = True


class Prod(object):
	APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
	SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:donthack@localhost:5432/chena'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	DEBUG=False
	SECRET_KEY = '@#$&*#*@&VVDYhdd)#*83#0(/ckk*'
	# WTF_CSRF_ENABLED = True

	