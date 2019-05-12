from django.db import models
from polls.models.project import Project

class Module(models.Model):
	"""
	模块表
	"""
	project = models.ForeignKey(Project,on_delete=models.CASCADE)
	name = models.CharField(max_length=50,null=False)
	describe = models.TextField(max_length=50)
	status = models.BooleanField(default=1)
	create_time = models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return self.name