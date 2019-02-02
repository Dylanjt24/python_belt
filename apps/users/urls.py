from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'register/$', views.register, name='register'),
    url(r'login/$', views.login, name='login'),
    url(r'dashboard/$', views.dashboard, name='dashboard'),
    url(r'logout/$', views.logout, name='logout'),
    url(r'addJob/$', views.add_job, name='add_job'),
    url(r'create_job/$', views.create_job, name='create_job'),
    url(r'user_job/(?P<job_id>\d+)/$', views.user_job, name='user_job'),
    url(r'delete/(?P<job_id>\d+)/$', views.delete, name='delete'),
    url(r'view/(?P<job_id>\d+)/$', views.view, name='view'),
    url(r'edit/(?P<job_id>\d+)/$', views.edit, name='edit'),
    url(r'confirm/(?P<job_id>\d+)/$', views.confirm, name='confirm')
]
