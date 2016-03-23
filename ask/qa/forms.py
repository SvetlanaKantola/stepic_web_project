from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
	title = forms.CharField(max_length = 255) 
	text = forms.CharField(widget=forms.Textarea)
	author = 1
	def __init__(self,user,**kwargs):
		self._user = user
		super(AskForm,self).__init__(**kwargs)
	def clean_title(self) :
		title = self.cleaned_data['title']
		return title

	def clean_text(self) :
		text = self.cleaned_data['text']
		return text
		
	def save(self):
		self.cleaned_data['author']=self._user
		quest = Question.objects.create(title=self.cleaned_data['title'], text=self.cleaned_data['text'], author=self.author)
		#quest.save()
		return quest



class AnswerForm(forms.Form):
	text = forms.CharField(min_length=1, widget=forms.Textarea)
	question = forms.IntegerField(widget=forms.HiddenInput())
	author = 1
	
	def clean_text(self) :
		text = self.cleaned_data['text']
		return text
		
	def clean_question(self) :
		try :
			quest_id = int(self.cleaned_data['question'])
		except ValueError :
			raise forms.ValidationError('fail input')
		return quest_id
	
	def save(self) :
		answer = Answer.objects.create(text=self.cleaned_data['text'], question=self.cleaned_data['question'], author=self.author)
		#answer.save()
		return answer
