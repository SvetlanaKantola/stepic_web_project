from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

   url(r'^login/', 'qa.views.test', name='login'),
   url(r'^signup/', 'qa.views.test', name='signup'),
   url(r'^question/(?P<id>[0-9]+)/$', 'qa.views.question'),
   url(r'^ask/', 'qa.views.ask'),
   url(r'^answer/', 'qa.views.answer'),
   url(r'^popular/', 'qa.views.popular', name='popular'),   
   url(r'^new/', 'qa.views.test', name='new'),  
   url(r'^$', 'qa.views.pagebyindex', name='index'),

)
 