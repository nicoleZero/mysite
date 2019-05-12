from django.db import models


class Project(models.Model):
	"""
	项目表
	"""
	name = models.CharField("名称",max_length=50,null=False)
	describe = models.TextField("描述",max_length=50)
	status = models.BooleanField("状态",default=1)
	create_time = models.DateTimeField(auto_now_add= True)


	def __str__(self):
		return self.name