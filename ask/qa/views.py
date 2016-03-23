from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from models import Question, Answer 
from django.core.paginator import Paginator
from forms import AskForm, AnswerForm, SignupForm, LoginForm
from django.contrib.auth import authenticate, login

def test(request, *args, **kwargs):
        return HttpResponse('OK')

def my(request, *args, **kwargs):
        a = 'Hello, World: '
        b = args[0]

        x = render(request, 'tpl.html', {
        'title': a+b,
        })
        return HttpResponse (x)

def my_page(request, *args, **kwargs):
        try:
                page = int(request.GET.get('page', 1))
        except ValueError:
                raise Http404
        try:
                test = Test.objects.get(pk=page)
        except Post.DoesNotExist:
                test = None             
        
        all_test = Test.objects.all()
        r = ''
        #for test in all_test:
        #       r += test.title
        
        r = render(request, 'tpl.html', {
        'all_test': all_test,
        })

	return HttpResponse(r)

def post_list_all(request):
	posts = Question.objects.all()
	posts = posts.order_by('-id')
	limit = request.GET.get('limit', 10)
	page = request.GET.get('page', 1)
	paginator = Paginator(posts, limit)
	paginator.baseurl = '/?page='
	page = paginator.page(page) # Page
	return render(request, 'tpl_post_list_all.html', {
	'posts': page.object_list,
	'paginator': paginator, 
	'page': page,
	})

def post_list_popular(request):
        posts = Question.objects.all()
	posts = posts.order_by('-rating')
        limit = request.GET.get('limit', 10)
        page = request.GET.get('page', 1)
        paginator = Paginator(posts, limit)
        paginator.baseurl = '/popular/?page='
        page = paginator.page(page) # Page
        return render(request, 'tpl_post_list_all.html', {
        'posts': page.object_list,
        'paginator': paginator,
        'page': page,
        })

def post(request, *args, **kwargs):
        post_id  = args[0]
	#post_url = '/answer/?question='+str(post_id)
	post_url = '/question/'+str(post_id)+'/'
	try:
		post = Question.objects.get(id=post_id)
	except Question.DoesNotExist:
		raise Http404
	if request.method == "POST":
                form = AnswerForm(request.POST)
		form._user = request.user 
		form._question = args[0] 
		if form.is_valid():
                        post = form.save()
                        #url = post.get_url()
                        return HttpResponseRedirect(post_url)
        else:
        	form = AnswerForm()
	return render(request, 'tpl_post.html', {
       	'post': post,
       	'answers' : post.answer_set.all(),
       	'form' : form,
	'post_url' : post_url
       	})

def post_ask_add(request, *args):
	if request.method == "POST":
		form = AskForm(request.POST)
		form._user = request.user
		if form.is_valid():
			post = form.save()
			#url = post.get_url()
			return HttpResponseRedirect('/question/'+str(post.id)+'/')
	else:
		form = AskForm()
	return render(request, 'tpl_post_ask_add.html', {
		'form': form
	})

def post_answer_add(request):
        if request.method == "POST":
                form = AnswerForm(request.POST)
                if form.is_valid():
                        post = form.save()
                        #url = post.get_url()
                        return HttpResponseRedirect('/question/'+request.GET.get('question')+'/')
        else:
                return HttpResponseRedirect('/')
       

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

class RegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/login/"

    template_name = "register.html"

    def form_valid(self, form):
        form.save()

        return super(RegisterFormView, self).form_valid(form)

def signup(request):
        if request.method == "POST":
                form = SignupForm(request.POST)
                if form.is_valid():
                        post = form.save()
                        #url = post.get_url()
                        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
			login(request,user)
			return HttpResponseRedirect('/')
        else:
                form = SignupForm()
        return render(request, 'tpl_signup.html', {
                'form': form
        })

def auth_login(request):
	user = request.user 
	if user.is_authenticated():
		return HttpResponseRedirect('/')
        if request.method == "POST":
                form = LoginForm(request.POST)
                if form.is_valid():
                        #post = form.save()
                        #url = post.get_url()
                        username = request.POST['username']
    			password = request.POST['password']
    			user = authenticate(username=username, password=password)
    			if user is not None:
        			if user.is_active:
            				login(request, user)
            			        return HttpResponseRedirect('/')
					# Redirect to a success page.
        			else:
            				# Return a 'disabled account' error message
            				return HttpResponseRedirect('/login/')
    			else:
        			# Return an 'invalid login' error message.
        			return HttpResponseRedirect('/login/')
        else:
                form = LoginForm()
        return render(request, 'tpl_login.html', {
                'form': form
        })
