from django.conf.urls import url
from app import views
from django.views.decorators.cache import cache_page

'''
url反向解析
在template中：使用url标签
在python中：使用django.core.urlresolvers.reverse()
在更高层次处理model实例时，可以使用get_absolute_url()方法
'''

app_name = 'app'
urlpatterns = [
    url(r'^index/$', views.Index, name='index'),
    url(r'^article/(?P<pk>\d+)/$', views.Blog, name='article'), # 将括号对(?P<pk>\d+)里面的参数作为第二个参数传递给视图函数Blog(request,pk)
    url(r'^detail/(?P<pk>\d+)/?$', views.detail, name='detail'),
    url(r'^about/$', views.about, name='about'),
    url(r'^tag/(?P<name>.*?)/$', views.tag, name='tag'),
]