from django.http import HttpResponse # for handling request/response objects
from django.template import Context, loader, RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from blog.models import Post
from blog.forms import PostForm

# Create your views here.

# helper function 
def encode_url(url):
	return url.replace(' ', '_')


def index(request):
	latest_posts = Post.objects.all().order_by('-created_at')
	popular_posts = Post.objects.order_by('-views')[:5]
	t = loader.get_template('blog/index.html')
	context_dict = {
		'latest_posts': latest_posts, 
		'popular_posts': popular_posts,
	}
	for post in latest_posts:
		post.url = encode_url(post.title)
	for popular_post in popular_posts:
		popular_post.url = encode_url(popular_post.title)
	c = Context(context_dict)
	return HttpResponse(t.render(c))


def post(request, post_url):
	single_post = get_object_or_404(Post, title=post_url.replace('_', ' '))
	single_post.views +=1 # increment number of views 
	single_post.save()    # and save it
	t = loader.get_template('blog/post.html')
	c = Context({'single_post': single_post, })
	return HttpResponse(t.render(c)) 


def add_post(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid(): # form valid?
			form.save(commit=True) # save to DB
			return redirect(index)
		else:
			print form.errors # no, then display errors to end user

	else:
		form = PostForm()
	return render_to_response('blog/add_post.html', {'form': form}, context)




