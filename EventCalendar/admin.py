from django.contrib import admin

from .models import EventPage, EventComment
from .models import EventTag


admin.site.register(EventPage)
admin.site.register(EventTag)
admin.site.register(EventComment)