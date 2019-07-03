from django.urls import path
from testcase import views

urlpatterns = [
	path('',views.testcase_manage),
	path('debug',views.testcase_debug),
    path('assert',views.testcase_assert),
]