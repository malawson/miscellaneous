from django.conf.urls import url
# importing blog.views from project root dir
from blog import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add_post/', views.add_post, name='add_post'), # add post form
	#url(r'^(?P<slug>[\w|\-]+)/$', views.post, name='post'),
	url(r'^(?P<post_url>\w+)/$', views.post, name='post'),
]