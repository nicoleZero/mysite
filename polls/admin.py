from django.contrib import admin
from polls.models.project import Project
from polls.models.module import Module


class ProjectAdmin(admin.ModelAdmin):
	list_display = ['name','describe','status','create_time']
	search_fileds = ['name']
	list_filter = ['status']




class ModuleAdmin(admin.ModelAdmin):
	list_display = ['name','describe','status','create_time','project']
	search_fileds = ['name']
	list_filter = ['project']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Module,ModuleAdmin)

# Register your models here.
