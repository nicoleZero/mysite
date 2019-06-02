from django import forms
from polls.models import Project
from django import forms
from polls.models import Module

class ProjectForm(forms.ModelForm):
	"""
	name = forms.CharField(label='名称',max_length=100)
	describe = forms.CharField(label="状态",widget=forms.Textarea)
	status = forms.BooleanField(label="状态",required=False)
	"""
	class Meta:
		model = Project
		fields = ['name','describe','status']

class ModuleForm(forms.ModelForm):
	"""
	name = forms.CharField(label='名称',max_length=100)
	describe = forms.CharField(label="状态",widget=forms.Textarea)
	status = forms.BooleanField(label="状态",required=False)
	"""
	class Meta:
		model = Module
		fields = ['project','name','describe','status']