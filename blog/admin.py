from django.contrib import admin
from blog.models import *

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Classification)
admin.site.register(Critic)
admin.site.register(Comment)


