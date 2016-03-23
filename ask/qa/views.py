from django.shortcuts import render, get_object_or_404, redirect
#from django.views.decorators.http import require_GET
from django. core. paginator import Paginator  , EmptyPage
from django.http import HttpResponse, Http404, HttpResponseRedirect 
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from qa.forms import AskForm, AnswerForm
from django.contrib.auth import authenticate

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
#	try:
#		answers=Answer.objects.filter(question=question)
#	except ObjectDoesNotExist:
#		raise Http404(request)
	answers=question.answer_set.all()
	form = AnswerForm()
	return render(request, "qa/question.html", {
		'title':question.title	,
		'text':question.text,
		"answers" : answers,
		"form":form
	})

def answer(request):
	user = request.user
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		if form.is_valid():
			if user.is_authenticated() :
				form.author = user
				answer = form.save()
				url = '/question/' + form.question
				return HttpResponseRedirect(url)
			else :
				raise Http404
	
def ask(request):
	user = request.user
	if request.method == 'POST':
		form = AskForm(user,request.POST)
		if form.is_valid():	
			if user.is_authenticated() :
				form.author = user
				quest = form.save()
				url = quest.get_absolute_url()
				return HttpResponseRedirect(url)
			else :
				raise Http404
	else:
		form = AskForm(user)
	return render(request, "qa/ask.html" , {'form': form})
	
def test(request, *args, **kwargs):
    return HttpResponse('200 OK')
