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
    path('projects/<int:pk>/', views.project_detail_view, name='project_detail'),
    path('projects/<int:project_pk>/send_notice', views.send_notice, name='project_send_notice'),
    path('projects/<int:pk>/applicants', views.look_project_applicants_view, name='check_applicants_for_project'),
    path('projects/<int:project_pk>/applicants/<int:entry_pk>/<str:new_status>', views.change_status_event_entry_view, name='accept_or_deny_applicant'),
    path('projects/<int:pk>/participants', views.look_project_participants_view, name='look_participants_of_project'),
    #path('e/<int:pk>/', views.ProjectDetailedView.as_view(), name='project_detail'),
    path('projects/', views.ProjectListView.as_view(), name='project_list'), ##TODO: RENAME ALL EVENTS TO PROJECTS IN THIS MODULE
    path('projects/my_projects', views.my_projects_view, name='my_projects_list'),
    path('projects/<int:pk>/enter', views.enter_the_project_view, name='enter_the_project_view'),
    path('projects/create/', views.ProjectCreate.as_view(), name='project_create'),
    #path('projects/create/', views.create_project_view, name='project_create'),
    path('projects/pending', views.accept_new_projects_view, name='new_pending_projects_mod'),
    path('projects/pending/<int:pk>/accept', views.accept_project_view, name='accept_project_mod'),
    path('projects/pending/<int:pk>/deny', views.deny_project_view, name='deny_project_mod'),
    path('projects/<int:pk>/update', views.ProjectUpdate.as_view(), name='project_update'),
    path('projects/<int:pk>/delete', views.ProjectDelete.as_view(), name='project_delete'),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]