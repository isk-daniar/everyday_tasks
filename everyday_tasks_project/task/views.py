from django.views.generic import ListView

from task.models import Task


class TaskList(ListView):
    model = Task
    template_name = "task/assignments/assignments.html"

