from django.shortcuts import render, get_object_or_404
#from django.views.decorators.http import require_GET
from django. core. paginator import Paginator
from django.http import HttpResponse, Http404 
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from qa.models import Question, Answer

#@require_GET
def pagebyindex(request, *args, **kwargs):
    try:    
	questions = Question.objects.all().order_by('-id')
    except Question.DoesNotExist:
	raise Http404   		
    page = request.GET.get('page', 1)    
    paginator = Paginator(questions, 10)
#    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request,'qa/all.html',{
	'questions': page.object_list,
	'paginator': paginator,
	'page': page,
	})

#@require_GET
def popular(request, *args, **kwargs):
    try:    
	questions = Question.objects.all().order_by('-rating')
    except Question.DoesNotExist:
	raise Http404   		
    page = request.GET.get('page', 1)    
    paginator = Paginator(questions, 10)
#    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render(request,'qa/all.html',{
	'questions': page.object_list,
	'paginator': paginator, 
	'page': page,
	})

#@require_GET
def question(request, id):

	try:
		question = Question.objects.get(id=id)
	except ObjectDoesNotExist:
		raise Http404(request)
	return render(request, "qa/question.html", {
		'title':question.title	,
		'text':question.text,
		"answers" : question.answer_set.all(),
	})

def test(request, *args, **kwargs):
    return HttpResponse('200 OK')
