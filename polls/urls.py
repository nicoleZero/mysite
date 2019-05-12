from django.conf.urls import url
from . import views
from polls.views import project_views
urlpatterns = [url('index/',views.index,name='index'),
			   url('project/',views.project_manage,name='project_manage'),
			   url('module/',views.module_manage,name='module_manage'),
			   url('project/add_project',project_views.add_project,name='add_project'),
			   url('logout/',views.logout,name='logout'),
			   ]