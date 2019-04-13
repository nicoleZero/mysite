from django.conf.urls import url
from . import views
urlpatterns = [url('index/',views.index,name='index'),
			   url('manage/',views.manage,name='manage'),
			   url('logout/',views.logout,name='logout'),
			   ]