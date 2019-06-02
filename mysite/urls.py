"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from polls.views import login_views
from polls.views import project_views
from polls.views import module_views

from django.urls import path

urlpatterns = [
    #url('polls/',include('polls.urls')),

    path(r'admin/', admin.site.urls),
    path('index/',login_views.index),
    #project管理
    path('project/',project_views.project_manage),
    path(r'project/add_project/',project_views.add_project),
    path(r'project/delete_project/<int:pid>/',project_views.delete_project),
    path(r'project/modify_project/<int:pid>/',project_views.modify_project),

    path('module/',module_views.module_manage),
    path(r'module/add_module/', module_views.add_module),
    path(r'module/delete_module/<int:pid>/', module_views.delete_module),
    path(r'module/modify_module/<int:pid>/', module_views.modify_module),

    path('testcase/',include('testcase.urls')),

    path('logout/',login_views.logout),
    path('', login_views.index),

]
