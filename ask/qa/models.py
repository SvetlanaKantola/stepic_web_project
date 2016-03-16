from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
	title = models.CharField(max_length=100)
	text = models.CharField(max_length=255)
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=1)
	author =  models.CharField(max_length=20)
	likes = models.ForeignKey(User,default=1)

	def __unicode__(self) :
		return self.title

	def get_url(self) :
		return reverse('question', kwargs={'id': self.id})


class Answer(models.Model):
	text = models.CharField(max_length=100)
	added_at =  models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question)
	author = models.CharField(max_length=20)
	
	def __unicode__(self) :
		return self.author + self.added_at + self.text


