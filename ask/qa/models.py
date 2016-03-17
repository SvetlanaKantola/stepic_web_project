from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
	title = models.CharField(max_length=100, null=True)
	text = models.CharField(max_length=255, null=True)
	added_at = models.DateTimeField(auto_now_add=True, null=True)
	rating = models.IntegerField(default=1)
	author =  models.CharField(User, null=True)
	likes = models.ForeignKey(max_length=1000, null=True)

	def __unicode__(self) :
		return self.title

	def get_url(self) :
		return reverse('question', kwargs={'id': self.id})


class Answer(models.Model):
	text = models.CharField(max_length=100, null=True)
	added_at =  models.DateTimeField(auto_now_add=True, null=True)
	question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
	author = models.CharField(User, null=True)
	
	def __unicode__(self) :
		return self.author + self.added_at + self.text


