#bind = "0.0.0.0:8000"
#pythonpath="/home/box/web/ask"
#working_dir="/home/box/web/ask"
 CONFIG = {
    'mode': 'django',
    'working_dir': '/home/box/web/ask',
    #'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:8000',
        #'--workers=16',
        #'--timeout=60',
	'--log-level=debug',
	'--access-logfile= /home/box/web/ask/la.log'
	' --error-logfile /home/box/web/ask/err.log'
        'ask',
    ),
}