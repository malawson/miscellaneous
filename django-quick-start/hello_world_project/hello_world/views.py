from django.template import Context, loader
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	t = loader.get_template('index.html')
	return HttpResponse(t.render())

	#return HttpResponse('<html><body>Hello, World!</body></html>')

def about(request):
	return HttpResponse(
			"""Here is the About Page. Want to return home? 
			<a href='/'>Back Home</a>
			"""
		)

def better(request):
	t = loader.get_template('betterhello.html')
	c = Context({'current_time' : datetime.now(), })
	return HttpResponse(t.render(c))