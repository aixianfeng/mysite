# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import Http404

from django.contrib.syndication.views import Feed

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from books.models import Article, Comment
from books.models import Tag
import datetime
#from datetime import datetime

# Create your views here
def comment_add(request):
	if request.method == 'POST':
		article_id = request.POST.get('article', '')
		detail = request.POST.get('detail', '')
		if article_id and detail:
			comment = Comment()
			comment.Article = Article(id=article_id)
			comment.detail = detail
			comment.save()
		return HttpResponseRedirect('/view/%s' % article_id)

def list(request):
	articles = Article.objects.order_by("-id").all()
	return render_to_response('list.html', {'articles': articles})

def view(request, id):
	article = Article.objects.get(id=id)
	comments = Comment.objects.filter(Article=id).order_by("-id")
	print len(comments)
	return render_to_response('view.html', {'article':article, 'comments': comments})

def add(request):
	if request.method == 'POST':
		content = request.POST.get('content', None)
		title = request.POST.get('title', None)
		new = Article(content=content, title=title)
		new.save()
		return HttpResponseRedirect('/list')
	return render_to_response('add.html', {'method_str':request.method})
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
