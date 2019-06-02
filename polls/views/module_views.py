from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from polls.models.module import Module
from polls.forms import ModuleForm
#模块管理页
@login_required
def module_manage(request):
	if request.method == "GET":
		module_all = Module.objects.all()
		return render(request, "module.html",{"modules":module_all,"type":"list"} )


@login_required
def add_module(request):
	"""
	添加模块
	:param request:
	:return:
	"""
	print("请求方法")
	if request.method == "GET":
		module = ModuleForm()
		return render(request, "module.html", {"form":module,"type": "add"})
	elif request.method == "POST":
		form = ModuleForm(request.POST)
		if form.is_valid():
			project = form.cleaned_data['project']
			name = form.cleaned_data['name']
			describe = form.cleaned_data['describe']
			status = form.cleaned_data['status']

			Module.objects.create(project=project,name=name,describe=describe,status=status)
			return HttpResponseRedirect("/module/")


@login_required
def modify_module(request, pid):
	if request.method == "GET":
		if pid:
			p = Module.objects.get(id=pid)
			form = ModuleForm(instance=p)
			return render(request, "module.html", {"type": "modify", "id":p.id,"form": form, "id": pid})

	elif request.method == "POST":
		form = ModuleForm(request.POST)
		if form.is_valid():
			project = form.cleaned_data['project']
			name = form.cleaned_data['name']
			describe = form.cleaned_data['describe']
			status = form.cleaned_data['status']

			p = Module.objects.get(id=pid)
			p.project = project
			p.name = name
			p.describe = describe
			p.status = status
			p.save()
		return HttpResponseRedirect("/module/")



def delete_module(request, pid):
	print("delete module ", pid)
	if request.method == "GET":
		try:
			p = Module.objects.get(id=pid)
		except Module.DoesNotExist:
			return HttpResponseRedirect("/module/")
		else:
			p.delete()
			return HttpResponseRedirect("/module/")
