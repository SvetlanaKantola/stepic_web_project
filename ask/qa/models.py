#from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

#class Post(object):                                      
#    title = models.CharField(max_length=255)             
#    content = models.TextField()                         
#    creation_date = models.DateTimeField(blank=True)     
#    def __unicode__(self):                               
#        return self.title()                              
#    def get_absolute_url(self):                          
#        return '/question/%d/' % self.pk                 
#    class Meta:                                          
#        db_table = 'qa__question'                        
#        ordering = ['-creation_date']                    

class Question(models.Model):
	title = models.CharField(max_length=200, null=True)
	text = models.CharField(max_length=1000, null=True)
	added_at = models.DateTimeField(null=True)
	rating = models.IntegerField(default=0)
#	author =  models.CharField(max_length=20)
#	likes = models.ForeignKey(User,default=1)
	author = models.ForeignKey(User, null=True)
	likes = models.CharField(max_length=1000, null=True)
	
	def __unicode__(self) :
		return self.title

#	def get_url(self) :
#		return reverse('question', kwargs={'id': self.id})


class Answer(models.Model):
	text = models.CharField(max_length=1000, null=True)
	added_at =  models.DateTimeField(null=True)
#	question = models.ForeignKey(Question)
#	author = models.CharField(max_length=20)
	question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
	author= models.ForeignKey(User, null=True)
	
#	def __unicode__(self) :
#		return self.author + self.added_at + self.text
