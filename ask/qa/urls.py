#project/project/urls.py

from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qa.views',

#   url(r'^$', 'test', name='index'),

#   url(r'^login/', 'test', name='login'),

#   url(r'^signup/', 'test', name='signup'),

#   url(r'^question/(?P<id>[0-9]+)/$', 'test', name='question'),

#   url(r'^ask/', 'test', name='ask'),

#   url(r'^popular/', 'test', name='popular'),   

#   url(r'^new/', 'test', name='new'),  



#   url(r'^$', 'test', name='index'),
#   url(r'^login/.*$', 'test', name='login'),
#   url(r'^signup/.*$', 'test', name='signup'),
#   url(r'^question/\d+/$', 'test', name='question'),
#   url(r'^ask/.*$', 'test', name='ask'),
#   url(r'^popular/.*$', 'test', name='popular'),   
#   url(r'^new/.*$', 'test', name='new'),  
   

#    url(r'^$', views.test),
#    url(r'^login', views.test),
#    url(r'^signup', views.test),
#    url(r'^questions/\d+', views.test),
#    url(r'^ask', views.test),
#    url(r'^ask//popular', views.test),
#    url(r'^popular', views.test),
#    url(r'^new', views.test)


    url(r'^$', qa.views.test),
    url(r'^login/.*$', qa.views.test),
    url(r'^signup/.*$', qa.views.test),
    url(r'^questions/\d+/.*$', qa.views.test),
    url(r'^ask/.*$', qa.views.test),
    url(r'^ask//popular', qa.views.test),
    url(r'^popular/.*$', qa.views.test),
    url(r'^new/.*$', qa.views.test)

)

#//urlpatterns=[
#//]
