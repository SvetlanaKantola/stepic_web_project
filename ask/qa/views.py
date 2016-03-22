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
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		q.author = reques.user
		q = form.save()
		q.author = reques.user
		q.save()
		return HttpResponseRedirect('/question/' + str(q.question_id))
	#return render(request, "qa/ask.html", {
	#	"form":form
	#})
	
def ask(request):
	print("is : " + str(request.user.is_authenticated()))
	if request.method == 'POST':
		form = AskForm(request.POST)
		form.user = request.user
		if form.is_valid():	
			q = form.save()
			return HttpResponseRedirect('/question/' + str(q.id) +'/')
		else:
			return HttpResponseRedirect('/question/123/')
	else:
		form = AskForm()
	return render(request, "qa/ask.html" , {'form': form})
	
def test(request, *args, **kwargs):
    return HttpResponse('200 OK')
