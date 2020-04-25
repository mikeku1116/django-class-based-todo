from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=100)
    finish = models.BooleanField(default=False)
    created = models.DateField(default=timezone.now)
