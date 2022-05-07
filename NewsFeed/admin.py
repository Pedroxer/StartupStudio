from django.contrib import admin

from .models import NewsArticle
from .models import Tag
from .models import Comment

admin.site.register(NewsArticle)
admin.site.register(Tag)
admin.site.register(Comment)

# Register your models here.
