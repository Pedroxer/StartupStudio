from django.urls import path, reverse_lazy
from django.views.generic import RedirectView
from django.views.i18n import JavaScriptCatalog

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_request, name='register'),
    path('login', RedirectView.as_view(url=reverse_lazy('accounts/login/')), name='login_core'),
    path('logout', views.logout_view, name='logout'),
    path('e/<int:pk>/', views.ProjectDetailedView.as_view(), name='project_detail'),
    path('projects/', views.ProjectListView.as_view(), name='project_list'), ##TODO: RENAME ALL EVENTS TO PROJECTS IN THIS MODULE
    path('projects/<int:pk>', views.enter_the_project_view, name='enter_the_project_view'),
    path('projects/create/', views.ProjectCreate.as_view(), name='project_create'),
    #path('projects/create/', views.create_project_view, name='project_create'),
    path('projects/pending', views.accept_new_projects_view, name='new_projects_mod'),
    path('projects/pending/<int:pk>/accept', views.accept_project_view, name='accept_project_mod'),
    path('projects/pending/<int:pk>/deny', views.deny_project_view, name='deny_project_mod'),
    path('projects/<int:pk>/update', views.ProjectUpdate.as_view(), name='project_update'),
    path('projects/<int:pk>/delete', views.ProjectDelete.as_view(), name='project_delete'),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]