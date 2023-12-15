from django.contrib import admin

from task import models


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "type_task", "link", "reward", "status", "user"]



