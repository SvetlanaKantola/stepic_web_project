from django.forms import ModelForm
from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User

class AskForm(ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text']


class AnswerForm(ModelForm):
	class Meta:
		model = Answer
		fields = ['text', 'question']

