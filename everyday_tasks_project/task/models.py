from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Task(models.Model):
    """ Задании """

    TYPE_TASK = [
        ('Поставить лайк', 'Поставить лайк'),
        ('Сделать репост', 'Сделать репост'),
        ('Написать комментарий', 'Написать комментарий'),
    ]

    STATUS = [
        ('Все статусы', 'Все статусы'),
        ('Активные', 'Активные'),
        ('Остановленные', 'Остановленные'),
        ('Завершенные', 'Завершенные'),
        ('В очереди', 'В очереди'),
        ('На модерации', 'На модерации'),
        ('Заблокированные', 'Заблокированные'),
    ]

    title = models.CharField(max_length=100)
    type_task = models.CharField(max_length=36, choices=TYPE_TASK)
    link = models.CharField(max_length=100)
    reward = models.FloatField(default=0)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=36, choices=STATUS)
    url = models.SlugField(max_length=130, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.type_task == 'Поставить лайк':
            self.reward = 0.10
        elif self.type_task == 'Сделать репост':
            self.reward = 0.40
        elif self.type_task == 'Написать комментарий':
            self.reward = 0.50
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('task', kwargs={'task_slug': self.url})

    def __str__(self):
        return self.title


class TaskCompletion(models.Model):
    """ Выполненные задания """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    completion_date = models.DateTimeField()
    status = models.CharField(max_length=36)


