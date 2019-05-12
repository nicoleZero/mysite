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

urlpatterns = [
    #url('polls/',include('polls.urls')),

    url(r'^admin/', admin.site.urls),
    url('index/',login_views.index),
    #project管理

    url(r'project/add_project/',project_views.add_project),
    url(r'project/modify_project/', project_views.modify_project),
    url(r'project/delete_project/',project_views.delete_project),
    url('project/',project_views.project_manage),


    url('module/',module_views.module_manage),
    url('logout/',login_views.logout),
    url('', login_views.index),

]
