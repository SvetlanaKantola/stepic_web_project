from django.shortcuts import render

from django.http import HttpResponse 
def test(request, *args, **kwargs):
    return HttpResponse('OK')

#def test (environ,start_response):
#	status = '200 OK'
#	headers= [('Content-type','text/plain')]
#	start_response(status,headers)
#	body="\r\n".join(environ['QUERY_STRING'].split('&'))	
#	return [body]
