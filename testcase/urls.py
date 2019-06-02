from django.urls import path
from testcase import views

urlpatterns = [
	path('',views.testcase_manage),
]