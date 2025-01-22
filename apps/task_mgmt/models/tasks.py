from django.db import models

# importing the necessary models from the respective apps
from apps.authentication.models import UserMaster
from apps.base.models import BaseModel




class TaskMaster(BaseModel):
    user = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        db_table = "task_master"
