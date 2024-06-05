from django.db import models


class TaskCategory(models.Model):



    categoty_name = models.CharField(max_length=250)
    categoty_type = models.CharField(max_length=20)


