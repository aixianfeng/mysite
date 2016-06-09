# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import Http404

from django.contrib.syndication.views import Feed

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from books.models import Article
from books.models import Tag
import datetime
#from datetime import datetime

# Create your views here
def home(request):
	posts = Article.objects.all()
	paginator = Paginator(posts, 2)
	page = request.GET.get('page')

	try:
		post_list = paginator.page(page)
	except PageNotAnInteger:
		post_list = paginator.page(1)
	except EmptyPage:
		post_list = paginator.paginator(paginator.num_pages)
	return render(request, 'home.html', {'post_list': post_list})

def hello(request):
	return HttpResponse("Hello World!")

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body><html>" % now
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#	assert False
	html = "<html><body>In %s hours, it will be %s." % (offset, dt)
	return HttpResponse(html)
