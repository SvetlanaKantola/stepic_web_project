from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#urlpatterns = patterns('qa.views',
#   url(r'^$', 'test', name='index'),
#   url(r'^login/', 'test', name='login'),
#   url(r'^signup/', 'test', name='signup'),
#   url(r'^question/(?P<id>[0-9]+)/$', 'test', name='question'),
#   url(r'^ask/', 'test', name='ask'),
#   url(r'^popular/', 'test', name='popular'),   
#   url(r'^new/', 'test', name='new'),  
#)
urlpatterns = [
   url(r'^$', views.test, name='index'),
   url(r'^login/', views.test, name='login'),
   url(r'^signup/', views.test, name='signup'),
   url(r'^question/(?P<id>[0-9]+)/$', views.test, name='question'),
   url(r'^ask/', views.test, name='ask'),
   url(r'^popular/', views.test, name='popular'),   
   url(r'^new/', views.test, name='new'),  
]
