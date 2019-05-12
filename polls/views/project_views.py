from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from polls.models.project import Project

@login_required
def project_manage(request):
	#return render(request,"project.html")
	project_all = Project.objects.all()
	return render(request, "project.html", {"projects":project_all,"type":"list"})
	#return render(request, "project.html", {"type": "add"})

@login_required
def add_project(request):
	"""
	添加项目
	:param request:
	:return:
	"""
	print("请求方法")
	if request.method == "GET":
		return render(request, "project.html", {"type": "add"})
	elif request.method == "POST":
		name = request.POST.get("name","")
		describe = request.POST.get("describe","")
		status = request.POST.get("status","")
		if name == "":
			return render(request,"project.html",{"type":"add","name_error":"不可为空"})
		Project.objects.create(name=name,describe=describe,status=status)
		return HttpResponseRedirect("/project/")

@login_required
def modify_project(request):

	if request.method == "GET":
		return render(request, "project.html", {"type": "modify"})
		Project.objects.get(id=pid)
	elif request.method == "POST":
		name = request.POST.get("name","")
		describe = request.POST.get("describe","")
		status = request.POST.get("status","")
		if name == "":
			return render(request,"project.html",{"type":"add","name_error":"不可为空"})
		Project.objects.create(name=name,describe=describe,status=status)
		return HttpResponseRedirect("/project/")

def delete_project(request):
	pass