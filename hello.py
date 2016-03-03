def wsgi_app(environ,start_response):
try:
	status = '200 OK'
	headers= [('Content-Type','text/plain')]
#      body = []
#	for key,value in environ.items90:
#         body.append('%s=%r'%(key,value))
#
	body='\r\n'.join(environ['QUERY_STRING'].split('&'))	
	start_response(status,headers)
	return [body]
except:
	status = "500 Errorer"
	headers= [('Content-Type','text/plain')]
	start_response(status,headers,sys.exc_info())
	return ["My Error"]
	