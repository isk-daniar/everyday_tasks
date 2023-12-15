from django.urls import path, include

from task.views import TaskList

urlpatterns = [
    path("", TaskList.as_view(), name="task_list"),
]
