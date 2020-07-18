from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    task = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task
