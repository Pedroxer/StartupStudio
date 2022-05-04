from django.contrib import admin

from .models import Direction
from .models import EventType
from .models import Skill
from .models import EntryStatus
from .models import Team
from .models import Project
from .models import ProjectEntry
from .models import ProjectResult
from .models import ProjectChatMessage
from .models import TeamChatMessage
from .models import TeamEntry

admin.site.register(Direction)
admin.site.register(EventType)
admin.site.register(Skill)
admin.site.register(EntryStatus)
admin.site.register(Team)
admin.site.register(Project)
admin.site.register(ProjectEntry)
admin.site.register(ProjectResult)
admin.site.register(ProjectChatMessage)
admin.site.register(TeamChatMessage)
admin.site.register(TeamEntry)

