from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def index(request):
	if request.method == "GET":
		return render(request, "index.html")
	else:
		username = request.POST.get("username","")
		password = request.POST.get("password","")
		if username == "" or password == "":
			return render(request, "index.html", {"error": "用户名或密码为空"})
		user = auth.authenticate(username=username,password=password)
		if user is None:
			return render(request, "index.html", {"error": "用户密码错误"})
		else:
			auth.login(request,user)
			return HttpResponseRedirect("/project/")
	return render(request, 'index.html')
	#return HttpResponse("Hello, world.You are at the polls index.")
# Create your views here.
#登录成功,默认项目管理页


@login_required
def logout(request):
	auth.logout(request)#删除服务器保存的session
	#request.session.clear()
	return render(request, "index.html")
