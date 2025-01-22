from rest_framework.urls import path
from apps.task_mgmt.views import TaskView

urlpatterns = [
    path('task/', TaskView.as_view(), name='task-add-get'),
    path('task/<uuid:task_id>/', TaskView.as_view(), name='task-retrive-update-delete')
]
