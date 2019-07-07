from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from polls.models.project import Project

from polls.forms import ProjectForm

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
def modify_project(request,pid):

	if request.method == "GET":
		if pid:
			p = Project.objects.get(id=pid)
			form = ProjectForm(instance=p)
			return render(request, "project.html", {"type": "modify", "form": form,"id":pid})

	elif request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			describe = form.cleaned_data['describe']
			status = form.cleaned_data['status']

			p = Project.objects.get(id=pid)
			p.name = name
			p.describe = describe
			p.status = status
			p.save()
		return HttpResponseRedirect("/project/")
		"""
		name = request.POST.get("name","")
		describe = request.POST.get("describe","")
		status = request.POST.get("status","")
		if name == "":
			return render(request,"project.html",{"type":"add","name_error":"不可为空"})
		Project.objects.create(name=name,describe=describe,status=status)
		return HttpResponseRedirect("/project/")
		
		if form.is_valid():
			name = form.cleaned_data['name']
			describe = form.cleaned_data['describe']
			status = form.cleaned_data['status']

			p = Project.objects.get(id=pid)
			p.name = name
			p.describe = describe
			p.status = status
			p.save()
		return HttpResponseRedirect("/project/")
		"""

def delete_project(request,pid):

	print("delete project ",pid)
	if request.method == "GET":
		try:
			p = Project.objects.get(id=pid)
		except Project.DoesNotExist:
			return HttpResponseRedirect("/project/")
		else:
			p.delete()
			return HttpResponseRedirect("/project/")
		"""
	elif request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			describe = form.cleaned_data['describe']
			status = form.cleaned_data['status']

			p = Project.objects.get(id=pid)
			p.name = name
			p.describe = describe
			p.status = status
			p.save()
		return HttpResponseRedirect("/project/")
		"""

def get_project_list(request):
	"""
	获取项目列表
	"""
	if request.method == 'GET':
		projects = Project.objects.all()
		project_list = []
		for pro in projects:
			project_dict={
				"id":pro.id,
				"name":pro.name
			}
			project_list.append(project_dict)
			#project_list[pro.id] = pro.name
			#project_list.append(pro.name)
		return JsonResponse({"success":"true","data":project_list})
	else:
		return JsonResponse({"success":"false","data":"请求方法错误!"})