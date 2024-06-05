from django.contrib import admin

from .models.categoryModel import TaskCategory
from .models.taskModel import Tasks


admin.site.register(Tasks)
admin.site.register(TaskCategory)
