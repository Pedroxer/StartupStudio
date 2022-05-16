import datetime


from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm
# Create your forms here.
from django.core.exceptions import ValidationError

from django.forms import ModelForm, DateInput

from UserSystem.models import CustomUser
from core.models import Project


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CreateProjectForm(ModelForm):
    project_start = forms.DateField(widget=AdminDateWidget())
    class Meta:
        model = Project
        fields = ['project_name', 'project_info', 'event_type', 'direction_type', 'project_skills', 'project_start',
                  'project_end', ]
        labels = {'project_name': 'Название проекта', 'project_info': 'Информация о проекте',
                  'event_type': 'Название направления', 'project_skills': 'Навыки мероприятия',
                  'project_start': 'Начало проекта', 'project_end': 'Конец проекта'}
        widgets = {
            'project_end': AdminDateWidget(),
        }

    def clean_project_end(self):
        data = self.cleaned_data['project_end']
        if data < datetime.date.today():
            raise ValidationError('Время конца не может быть в прошлом')
        return data

    def clean_project_start(self):
        data = self.cleaned_data['project_start']
        if data < datetime.date.today():
            raise ValidationError('Время начала не может быть в прошлом')
        return data

