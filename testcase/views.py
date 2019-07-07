from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
import json

# Create your views here.
def testcase_manage(request):
	return render(request,"testcase.html",{"type":"debug"})

def testcase_debug(request):
	if request.method=="POST":
		url = request.POST.get("url","")
		method = request.POST.get("method","")
		headers = request.POST.get("header","")
		type_ = request.POST.get("type","")
		parameter = request.POST.get("parameter","")
		print(type(parameter))
		print(parameter)
		print(method)
		print(url)
		print(headers)
		print(type_)
		json_par = parameter.replace("\'","\"")
		json_headers = headers.replace("\'", "\"")
		try:
			para = json.loads(json_par)
			print(type(para))
			print(para)
		except json.decoder.JSONDecodeError:
			return JsonResponse({"result": "参数类型错误"})
		'''
		try:
			json_headers = json.loads(json_header)
		except json.decoder.JSONDecodeError:
			return JsonResponse({"result":"header类型错误"})
		'''
		if method=="GET":
			if json_headers == "":
				r = requests.get( url, params = para)
				print(r.encoding)
			else:
				r = requests.get( url,params = para,headers=json_headers)
		elif method=="POST":
			if type_=="form-data":
				if json_headers == "":
					r = requests.post(url,data=para)
				else:
					r = requests.post(url, data=para,headers=json_headers)
			if type_=="json":
				if json_headers == "":
					r = requests.post(url, json=para)
				else:
					r = requests.post(url,json=para,headers=json_headers)
		#r = r.content.decode('ISO-8859-1').encode('utf-8')
		#html_doc = str(r, 'utf-8')
		r.encoding='utf-8'
		return JsonResponse({"result":r.text})
	else:
		return JsonResponse({"result":"请求方法错误!"})

def testcase_assert(request):
	if request.method == "POST":
		result_text = request.POST.get("result","")
		assert_text = request.POST.get("assert","")
		assert_type = request.POST.get("retype","")
		#后端增加断言和结果不能为空的校验
		if result_text == "" or assert_text == "":
			return JsonResponse({"result":"断言的文本不能为空!"})
		print("asserttype",assert_type)
		if assert_type == "include":
			if assert_text in result_text:
				return JsonResponse({"result":"断言成功!"})
			else:
				return JsonResponse({"result":"断言失败!"})
		elif assert_type == "equal":
			if assert_text == result_text:
				return JsonResponse({"result":"断言成功!"})
			else:
				return JsonResponse({"result":"断言失败!"})
	else:
		return JsonResponse({"result":"请求方法失败"})

