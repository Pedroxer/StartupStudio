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
    path('', views.main_profile, name='main_profile'),
    path('MyProfile/create', views.create, name='create'),
    path('MyProfile/ent', views.enter_info, name='enter_info'), #на заполнение формы начальной
    path('MyProfile/extra_view', views.extra_view, name='extra_view'),
    path('MyProfile/change', views.change, name='change'),
    path('MyProfile/delete', views.delete_profile, name='delete'),
    path('MyProfile/update', views.update, name='update'),
]
