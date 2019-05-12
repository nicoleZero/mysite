from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from polls.models.module import Module
#模块管理页
@login_required
def module_manage(request):
	return render(request, "module.html")
