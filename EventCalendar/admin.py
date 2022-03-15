from django.contrib import admin

from .models import EventPage
from .models import EventTag

admin.site.register(EventPage)
admin.site.register(EventTag)
