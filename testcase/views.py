from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
import json
from testcase.models import TestCase
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

def testcase_save_case(request):
	method_dict={"GET":1,"POST":2,"PUT":3,"DELETE":4}
	parameter_type_dict={"form-data":1,"json":2}
	assert_type_dict={"include":1,"equal":2}

	if request.method == "POST":
		url = request.POST.get('url',"")#请求地址
		name = request.POST.get('case_name',"")#用例名称
		method = request.POST.get('req_type', "")#请求方法
		header = request.POST.get('header', "")#请求头
		parameter_type = request.POST.get('par_type', "")#参数类型
		parameter_body = request.POST.get('parameter', "")#参数

		#断言部分
		result_body = request.POST.get('result', "")#响应值
		assert_type = request.POST.get('re_type', "")#断言类型
		assert_text = request.POST.get('assert_result ', "")#断言内容

		#保存部分
		module_id = request.POST.get('module_id',"")#模块号
		print("module_id",type(module_id),module_id)
		print("name",name)
		print("url",url)
		print("name",name)
		print("header",header)
		print("paramtertype",parameter_type)
		print("parameter",parameter_body)
		print("asserttype",assert_type)
		print("assert",assert_text)

		#由char变为int
		#print("1",method,method_dict['GET'])
		#print("2",parameter_type,parameter_type_dict[parameter_type])
		#print("3",assert_type,assert_type_dict[assert_type])
		#method_int = method_dict[method]
		#parameter_type_int = parameter_type_dict[parameter_type]
		#assert_type_int = assert_type_dict[assert_type]
		if url == "":
			return JsonResponse({"success":"false","data":"请求地址必填"})
		elif name == "":
			return JsonResponse({"success": "false", "data": "用例名称必填"})
		else:
			TestCase.objects.create(name="case_name", module_id=1, url="http://httpbin.org", method=1, header=1,
									parameter_type=1, parameter_body="parameter_body",
									result_body="result_body", assert_type=1, assert_text="assert_text")

			#TestCase.objects.create(name=name,module_id=module_id, url=url, method=method,header=header,parameter_type=parameter_type,parameter_body=parameter_body,result_body=result_body,assert_type=assert_type,assert_text=assert_text)
			return JsonResponse({"success":"true","data":"保存成功"})
	else:
		return JsonResponse({"result":"请求方法失败"})

