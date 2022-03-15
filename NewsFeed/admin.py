from django.contrib import admin

from .models import NewsArticle
from .models import Tag

admin.site.register(NewsArticle)
admin.site.register(Tag)

# Register your models here.
