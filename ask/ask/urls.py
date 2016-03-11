from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#urlpatterns = patterns('',
urlpatterns = [
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'qa.views.test'),
    url(r'^login/.*$', 'qa.views.test'),
    url(r'^signup/.*$', 'qa.views.test'),
    url(r'^questions/\d+/.*$', 'qa.views.test'),
    url(r'^ask/.*$', 'qa.views.test'),
    url(r'^ask//popular', 'qa.views.test'),
    url(r'^popular/.*$', 'qa.views.test'),
    url(r'^new/.*$', 'qa.views.test')

#    url(r'^admin/', include(admin.site.urls)),
]