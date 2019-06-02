from django.conf.urls import url
from . import views
from polls.views import project_views
from django.urls import path
urlpatterns = [path('index/',views.index,name='index'),
			   path('project/',views.project_manage,name='project_manage'),
			   path('module/',views.module_manage,name='module_manage'),
			   path('project/add_project',project_views.add_project,name='add_project'),
			   path('logout/',views.logout,name='logout'),
			   ]