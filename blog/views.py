from django.shortcuts import render_to_response
from blog.models import *
from django.template import RequestContext

def blog_list(request):
	classifications = navigation_bar()
	blogs = Article.objects.all().order_by('-publish_time')
	return render_to_response('index.html', {'blogs': blogs, 'classifications': classifications}, context_instance = RequestContext(request))


def blog_detail(request):
	classifications = navigation_bar()
	if request.method == 'GET':
		ids = request.GET.get('id','')
		try:
			blog = Article.objects.get(id = ids)
			comments = getComment(blog.id)
		except Article.DoesNotExist:
			raise Http404
		return render_to_response("detail.html", {"blog": blog, 'classifications': classifications, 'comments': comments}, context_instance=RequestContext(request))
	else:
		raise Http404

def blog_clas(request):
	classifications = navigation_bar()
	if request.method == 'GET':
		ids = request.GET.get('id','')
		try:
			blogs = Article.objects.filter(classification_id = ids)
		except Article.DoesNotExist:
			raise Http404
		return render_to_response("index.html", {"blogs": blogs, 'classifications': classifications}, context_instance=RequestContext(request))
	else:
		raise Http404


def test(request):
	blogs = Article.objects.all().order_by('-publish_time')
	return render_to_response('test.html', {'blogs': blogs}, context_instance = RequestContext(request))

def navigation_bar():
	classifications = Classification.objects.all()
	return classifications 
def getComment(blogid):

	def tree(comment, comment_list):
#		if not comment.is_root:
			parent = Comment.objects.get(id = comment.comment_parent)
			comment_list.append(parent)
			if parent.is_root:
				return comment_list
			else:
				return tree(parent, comment_list)
#		return [comment,]	

	comments = Comment.objects.filter(is_leaf = True, article = blogid)
	list_all = []
	for comment in comments:
		if not comment.is_root:
			comment_list = [comment,]
			list0 = tree(comment, comment_list)
			list_part = []
			for i in range(0, len(list0)-1):
				list1 = list0[i:i+2]
				list_part.append(list1)
			list_all.append(list_part)
		else:
			list_all.append([['', comment], ['', comment]])
	return list_all



