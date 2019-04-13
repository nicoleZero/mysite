from django.conf.urls import url
from . import views
urlpatterns = [url('index/',views.index,name='index'),
			   url('project/',views.project_manage,name='project_manage'),
			   url('module/',views.module_manage,name='module_manage'),
			   url('logout/',views.logout,name='logout'),
			   ]