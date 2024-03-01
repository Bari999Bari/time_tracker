import datetime

from django.db import models

from users.models import User


class Task(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=512, null=False)


class TaskActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities", null=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="activities", null=False)
    started_at = models.DateTimeField(auto_now=False, auto_now_add=True, null=False)
    finished_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
