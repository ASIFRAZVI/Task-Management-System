from rest_framework import serializers

from apps.task_mgmt.models import TaskMaster

class TaskMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskMaster
        exclude = ['id', 'created']