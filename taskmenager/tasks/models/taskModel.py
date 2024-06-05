from django.db import models

from .categoryModel import TaskCategory


class Tasks(models.Model):



    task_title = models.CharField(max_length=250)
    task_description = models.TextField()
    task_category = models.ManyToManyField(TaskCategory)
    task_importance_level = models.CharField(max_length=2)