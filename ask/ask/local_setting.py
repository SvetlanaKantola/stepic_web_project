import os.path
BASE_DIR=os.path.abspath(__file__)
BASE_DIR=os.path.dirname(BASE_DIR)
BASE_DIR=os.path.dirname(BASE_DIR)

#ROOT_URLCONF = 'ask.py'
DATABASES = {
	'default':{
		'ENGINE':'django.db.backends.sqlite3',
		'NAME':os.path.join(BASE_DIR,'db.sqlite3'),
	}
}
#TEMPLATE_DIRS = (
#	BASE_DIR = '/templetes',
#)
