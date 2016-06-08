# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
# Create your models here.

class Tag(models.Model):
	tag_name = models.CharField(max_length=64)
	
	def __str__(self):
		return self.tag_name

class Article(models.Model):
	title = models.CharField(max_length=100)
	category = models.CharField(max_length=50, blank=True)
	tag = models.ManyToManyField(Tag, blank=True)
	date_time = models.DateTimeField(auto_now_add=True)
	content = models.TextField(blank=True, null=True)

	def get_absolute_url(self):
		path = reverse('detail', kwargs={'id': self.id})
		return "http://127.0.0.1:8000%s" % path

	def __str__(self):
		return self.title.encode('utf-8')

	class Meta:
		ordering = ['-date_time']


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
