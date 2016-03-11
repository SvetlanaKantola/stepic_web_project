#gunicorn -b 0.0.0.0:8080 hello:app
#gunicorn -b 0.0.0.0:8080 hello:app
#bind=['127.0.0.1:8080','0.0.0.0:8080']
#bind=['0.0.0.0:8080'];
#pythonpath='/home/box/web'
#APP_MODULE='hello:wsgi_app'
#D=true
#t=30
# CONFIG = {
# 'mode': 'wsgi',
# 'working_dir': '/home/box/web/ask',
# 'python': '/usr/bin/python',
#'args':(
#	'--bind=0.0.0.0:8000',
#	'--workers=16',
#	'--timeout=60',
#	'ask.wsgi',
#	'app.module',
#),
#}
bind = "0.0.0.0:8000"
pythonpath='/home/box/web/ask'
accesslog = "/home/box/web/gunicorn_a.log"
errorlog = "/home/box/web/gunicorn_e.log"
pidfile = "/home/box/web/gunicorn_p.pid"
workers=16
timeout=60

#
# bind = "unix:/home/proft/projects/blog/run/blog.socket"
#workers = 5
#user = "www"
#group = "www"
#logfile = "/home/box/web/gunicorn.log"
#loglevel = "info"
#proc_name = "app_wsgi"
#pidfile = "/home/box/web/gunicorn.pid"