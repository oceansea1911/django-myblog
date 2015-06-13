from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.contrib import comments
from blog import views

import os
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.blog_list),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static').replace('\\', '/')}),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^blog/detail/', views.blog_detail),
    url(r'^test/', views.test),
    url(r'^blog/clas_display/', views.blog_clas),
    url(r'^blog/$', views.blog_list),
)
