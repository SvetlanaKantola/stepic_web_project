from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django. core. paginator import Paginator
from django.http import HttpResponse, Http404 

from qa.models import Question, Answer

@require_GET
def main(request, *args, **kwargs):
    try:    
	questions = Question.objects.order_by('-id')
    except Question.DoesNotExist:
	raise Http404   		
    page = request.GET.get('page', 1)    
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request,'questions.html',{
	'questions': page.object_list,
	'paginator': paginator, 'page': page,
	})

@require_GET
def populars(request, *args, **kwargs):
    try:    
	populars = Question.objects.order_by('-rating')
    except Question.DoesNotExist:
	raise Http404   		
    page = request.GET.get('page', 1)    
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render(request,'questions.html',{
	'questions': page.object_list,
	'paginator': paginator, 'page': page,
	})

@require_GET
def question(request, *args, **kwargs):
    id = kwargs['id']
    question = get_object_or_404(Question, id=id)		
    answers = Answer.objects.filter(question=question)
    return render(request,'question.html',{
	'question': question,
	'answers': answers,
	})

def test(request, *args, **kwargs):
    return HttpResponse('200 OK')
