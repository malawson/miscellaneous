from django.conf.urls import url
# importing blog.views from project root dir
from blog import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<post_url>\w+)/$', views.post, name='post'),
]