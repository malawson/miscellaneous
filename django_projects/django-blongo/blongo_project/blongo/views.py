from django.shortcuts import render
from django.http import HttpResponse
# templating system
from django.template import Context, loader
# post table
from blongo.models import Post

# Create your views here.


def index(request):
	latest_posts = Post.objects 
	t = loader.get_template('index.html')
	# mapping to frontend variable
	context_dict = {'latest_posts' : latest_posts}
	c = Context(context_dict)
	# rendering DB data on the front-end
	return HttpResponse(t.render(c))


