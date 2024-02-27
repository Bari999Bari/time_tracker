from django.contrib import admin

from core.models import Task, TaskActivity

admin.site.register(Task)
admin.site.register(TaskActivity)
