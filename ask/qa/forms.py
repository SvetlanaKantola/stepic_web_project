from django import forms
from models import Question, Answer
from django.forms import ModelForm
from django.contrib.auth.models import User

class SignupForm1(ModelForm):
	class Meta:
		model = User
		fields = ['username','email','password']

class SignupForm(forms.Form):
	username = forms.CharField(max_length=100)
	email = forms.EmailField()
	password = forms.CharField(max_length=100,widget=forms.PasswordInput)	
	def save(self):
		post = User.objects.create_user(**self.cleaned_data)
		#post = User(**self.cleaned_data)
		post.save()
		return post

class LoginForm(forms.Form):
        username = forms.CharField(max_length=100)
        password = forms.CharField(max_length=100,widget=forms.PasswordInput)
        
class AddPostForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(widget=forms.Textarea)
	def clean_message(self):
		text = self.cleaned_data['text']
		#if not is_ethic(message):
		#	raise forms.ValidationError('Message error', code=12)
		return message + \
			"\nThank you for your attention."
	def save(self):
		post = Question(**self.cleaned_data)
		post.save()
		return post

class AskForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(widget=forms.Textarea)
#	def __init__(self, *args, **kwargs):
#        	super(AskForm, self).__init__(*args, **kwargs)
        #def __init__(self,**kwargs):
	#	super(AskForm,self).__init__(self,**kwargs)
	#def clean(self):
	#	message = self.cleaned_data['message']
	#	if not is_ethic(message):
	#		raise forms.ValidationError('Message Error', code=12)
	#return message + "Thank you for your attention."
	def save(self):
		self.cleaned_data['author'] = self._user
		post = Question(**self.cleaned_data)
		post.save()
		return post

#class AskForm(ModelForm):
#	class Meta:
#		model = Question
#		fields = ['title', 'text']

class AnswerForm(forms.Form):
#        #title = forms.CharField(max_length=100)
        text = forms.CharField(widget=forms.Textarea)
#	def __init__(self,q_id, *args, **kwargs):
#                self.q_id = q_id
#		super(AnswerForm, self).__init__(*args, **kwargs)
#        #def __init__(self,**kwargs):
#	#	super(AnswerForm,self).__init__(**kwargs)
#	#def clean(self):
#        #       message = self.cleaned_data['message']
#        #       if not is_ethic(message):
#        #               raise forms.ValidationError('Message Error', code=12)
#        #return message + "Thank you for your attention."
        def save(self):
                self.cleaned_data['author'] = self._user 
		self.cleaned_data['question_id'] = self._question
		post = Answer(**self.cleaned_data)
                post.save()
                return post

#class AnswerForm(ModelForm):
#        class Meta:
#        	model = Answer
#        	fields = ['text', 'question']
