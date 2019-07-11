from django.db import models
from polls.models.module import Module

class TestCase(models.Model):
	"""
	测试用例表
	"""
	module = models.ForeignKey(Module,on_delete=models.CASCADE)
	name = models.CharField("名称",max_length=50,null=False)
	url = models.TextField("url",null=False)
	method = models.IntegerField("请求方法",null=False)#1:get;2:post;3:delete;4:put
	header = models.TextField("请求头",max_length=50,null=False)
	parameter_type = models.IntegerField("参数类型",null=False)#1:form_data;2:json
	parameter_body = models.TextField("参数内容",null=False)
	result_body = models.TextField("结果",null=False)
	assert_type = models.IntegerField("断言类型",null=False)
	assert_text = models.TextField("断言内容",null=False)
	create_time = models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return self.name