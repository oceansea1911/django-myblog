from django.db import models

class Author(models.Model):
	name = models.CharField(max_length = 20)
	email = models.EmailField(blank = True)
	website = models.URLField(blank = True)
	def  __unicode__(self):
		return u'%s' % (self.name)

class Classification(models.Model):
	name = models.CharField(max_length = 20)
	created_time = models.DateTimeField(auto_now_add = True)
	def __unicode__(self):
		return u'%s' % (self.name)

class Tag(models.Model):
	tag_name = models.CharField(max_length = 20)
	created_time = models.DateTimeField(auto_now_add = True)
	def __unicode__(self):
		return u'%s' % (self.tag_name)

class Article(models.Model):
	caption = models.CharField(max_length = 30)
	subcaption = models.CharField(max_length = 50, blank = True)
	publish_time = models.DateTimeField(auto_now_add = True)
	update_time = models.DateTimeField(auto_now = True)
	author = models.ForeignKey(Author)
	classification = models.ForeignKey(Classification)
	tags = models.ForeignKey(Tag)
	content = models.TextField()
	def __unicode__(self):
		return u'%s' % (self.caption)

class Critic(models.Model):
	name = models.CharField(max_length = 20)
	email = models.EmailField(blank = True)
	website = models.URLField(blank = True)
	def __unicode__(self):
		return u'%s' % (self.name)

class Comment(models.Model):
	article = models.ForeignKey(Article)
	critic = models.ManyToManyField(Critic)
	comment_time = models.DateTimeField(auto_now = True)
	ip = models.IPAddressField()
	comment_parent = models.IntegerField()
	content = models.TextField()
	is_leaf = models.BooleanField(default = False)
	is_root = models.BooleanField(default = False)
	def __unicode__(self):
		return u'%s' % (self.ip)

