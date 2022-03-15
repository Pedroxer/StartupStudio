from django.urls import  path

from . import views

app_name = 'EventCalendar'
urlpatterns = [
    path('', views.IndexUsingCulling, name='events'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('event_tag=<str:tag_name>/', views.tag_filtered, name='events_tag_filtered'),
    path('event/<int:event_id>/sendcomment', views.send_comment, name='send_comment'),
] 