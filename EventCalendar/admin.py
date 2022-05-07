from django.contrib import admin

from .models import EventPage, EventComment
from .models import EventTag

@admin.register(EventComment)
class EventCommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'user_id', 'comment_text', 'pub_datetime')
    pass


admin.site.register(EventPage)
admin.site.register(EventTag)
