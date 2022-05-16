from django.urls import path
from django.views.i18n import JavaScriptCatalog

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_request, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('e/<int:pk>/', views.EventDetailedView.as_view(), name='project_detail'),
    path('projects/', views.EventListView.as_view(), name='project_list'), ##TODO: RENAME ALL EVENTS TO PROJECTS IN THIS MODULE
    path('projects/create/', views.ProjectCreate.as_view(), name='project_create'),
    #path('projects/create/', views.create_project_view, name='project_create'),
    path('projects/<int:pk>/update', views.ProjectUpdate.as_view(), name='project_update'),
    path('projects/<int:pk>/delete', views.ProjectDelete.as_view(), name='project_delete'),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]