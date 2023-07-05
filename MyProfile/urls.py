import markdownx
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.views.i18n import JavaScriptCatalog

from . import views

app_name = 'MyProfile'
urlpatterns = [
    path('', views.main_profile, name='my_profile'),
]
