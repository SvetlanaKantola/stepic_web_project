def app (environ,start_response):
#try:
	status = '200 OK'
	headers= [('Content-type','text/plain')]
#      body = []
#	for key,value in environ.items90:
#         body.append('%s=%r'%(key,value))
#
	start_response(status,headers)
#	resp = environ['QUERY_STRING'].split('&')
#	resp = [item+"\r\n" for item in resp]
#	return resp
	body="\r\n".join(environ['QUERY_STRING'].split('&'))	
	return [body]
#except:
#	status = "500 Errorer"
#	headers= [('Content-Type','text/plain')]
#	start_response(status,headers,sys.exc_info())
#	return ["My Error"]
	