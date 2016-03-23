from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list_all, name='post_list_all'),
    url(r'^signup/$', views.signup,name='signup'),
    url(r'^login/$', views.auth_login, name='login'),
    url(r'^signup/$', views.test, name='test'),
    url(r'^question/(\d+)/$', views.post, name='post'),
    url(r'^ask/', views.post_ask_add, name='post_ask_add'),
    url(r'^popular/$', views.post_list_popular, name='post_list_popular'),
    url(r'^new/$', views.test, name='test'),
    #url(r'^answer', views.post_answer_add, name='test'),
]
