"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ask.qa import views


urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#    url(r'^$', views, name='test'),
    url(r'^$', 'qa.views.test'),
    url(r'^login/', 'qa.views.test'),
    url(r'^signup/', 'qa.views.test'),
    url(r'^question/', 'qa.views.test'),
    url(r'^questions/\d+/.*$', 'qa.views.test'),
    url(r'^ask/', 'qa.views.test'),
    url(r'^popular/', 'qa.views.test'),
    url(r'^new/', 'qa.views.test'),
]
#urlpatterns = patterns('qa.views',
#    url(r'^$', 'test'),
#    url(r'^login/', 'test', name ='login'),
#    url(r'^signup/', 'test', name ='signup'),
#    url(r'^questions/\d+/.*$', 'test', name ='question'),
#    url(r'^ask/', 'test', name ='ask'),
#    url(r'^popular/', 'test', name ='popular'),
#    url(r'^new/', 'test', name ='new'),
#)
