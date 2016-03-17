from django.conf.urls import patterns, include, url


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
   url(r'^$', 'qa.views.pagebyindex', name='index'),
   url(r'^login/', 'qa.views.test', name='login'),
   url(r'^signup/', 'qa.views.test', name='signup'),
   url(r'^question/(?P<id>[0-9]+)/$', 'qa.views.question', name='question'),
   url(r'^ask/', 'qa.views.test', name='ask'),
   url(r'^popular/', 'qa.views.popular', name='popular'),   
   url(r'^new/', 'qa.views.test', name='new'),  
]
