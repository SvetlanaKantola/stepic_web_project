from django.forms import ModelForm
from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User

#class AskForm(ModelForm):
class AskForm(forms.Form):
	title = forms.CharField()#min_length = 1) 
	text = forms.CharField(widget=forms.Textarea)#,min_length = 1)

#	class Meta:
#		model = Question
#		fields = ['title', 'text']
	def save(self):
		self.cleaned_data['author'] = self.user
		question = Question(**self.cleaned_data)
		question.save()
		#question = Question.objects.create(text=self.cleaned_data['text'], title=self.cleaned_data['title'], author=self.user)
		return question



class AnswerForm(forms.Form):
	text = forms.CharField(min_length=1, widget=forms.Textarea)
	question = forms.IntegerField(widget=forms.HiddenInput())
#class AnswerForm(ModelForm):
#	class Meta:
#		model = Answer
#		fields = ['text', 'question']
	def save(self):
		self.cleaned_data['author'] = self.user
		answer = Answer(**self.cleaned_data)
		answer.save()
		return answer
		
	def clean_question(self):
		return Question.objects.get(pk=int(self.cleaned_data['question']))
	
