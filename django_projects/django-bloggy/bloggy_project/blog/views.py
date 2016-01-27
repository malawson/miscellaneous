from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse # for handling request/response objects
from django.template import Context, loader
from blog.models import Post

# Create your views here.

def index(request):
	latest_posts = Post.objects.all().order_by('-created_at')
	t = loader.get_template('blog/index.html')
	context_dict = {'latest_posts': latest_posts, }
	for post in latest_posts:
		post.url = post.title.replace(' ', '_')
	c = Context(context_dict)
	return HttpResponse(t.render(c))

def post(request, post_url):
	single_post = get_object_or_404(Post, title=post_url.replace('_', ' '))
	t = loader.get_template('blog/post.html')
	c = Context({'single_post': single_post, })
	return HttpResponse(t.render(c)) 