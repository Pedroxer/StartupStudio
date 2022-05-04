from django.db import models
from UserSystem.models import CustomUser


class Direction(models.Model):
    direction_name = models.CharField(max_length=100)
    direction_info = models.CharField(max_length=800, blank=True)

    def __str__(self):
        return self.direction_name


class EventType(models.Model):
    event_type_name = models.CharField(max_length=50)
    event_type_info = models.CharField(max_length=800, blank=True)

    def __str__(self):
        return self.event_type_name


class Skill(models.Model):
    skill_name = models.CharField(max_length=80)
    skill_info = models.CharField(max_length=800, blank=True)

    def __str__(self):
        return self.skill_name


class EntryStatus(models.Model):
    entry_name = models.CharField(max_length=80)

    def __str__(self):
        return self.entry_name


class Team(models.Model):
    team_name = models.CharField(max_length=80)
    team_members = models.ManyToManyField(CustomUser, related_name="team_members")
    team_captain = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="team_captain")

    def __str__(self):
        return  self.team_name


class Project(models.Model):
    project_name = models.CharField(max_length=150)
    project_info = models.CharField(max_length=1500)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    direction_type = models.ForeignKey(Direction, on_delete=models.CASCADE)
    project_skills = models.ManyToManyField(Skill)
    project_authors = models.ManyToManyField(CustomUser)
    project_teams = models.ManyToManyField(Team, blank=True)

    def __str__(self):
        return self.project_name


class ProjectEntry(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.ForeignKey(EntryStatus, on_delete=models.CASCADE)

    def __str__(self):
        return self.project.project_name


class ProjectResult(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project_result = models.CharField(max_length=150)
    users_team = models.CharField(max_length=80)

    def __str__(self):
        return self.project_result


class ProjectChatMessage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=800)
    pub_time = models.DateTimeField('Date published')

    def __str__(self):
        return self.message_text


class TeamChatMessage(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=800)
    pub_time = models.DateTimeField('Date published')

    def __str__(self):
        return self.message_text


class TeamEntry(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.ForeignKey(EntryStatus, on_delete=models.CASCADE)

    def __str__(self):
        return  self.user.username + " to " + self.team.team_name







# Create your models here.
