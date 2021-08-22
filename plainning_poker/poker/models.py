from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import Enum

# Create your models here.


class User(AbstractUser):
    pass


class Role(Enum):
    observer = 0
    moderator = 1
    player = 2


class Task(models.Model):
    class STATUS:
        CREATE = 0
        IN_PROGRESS = 1
        DONE = 2

        CHOICES = (
            (CREATE, 'created'),
            (IN_PROGRESS, 'in_progress'),
            (DONE, 'done')
        )

    name = models.CharField(max_length=150)
    url = models.URLField()
    status = models.SmallIntegerField(choices=STATUS.CHOICES, default=STATUS.CREATE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    descriptions = models.TextField(null=True)
    grade = models.IntegerField(null=True)
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE)


class VoteResult(models.Model):
    pass


class Room(models.Model):
    pass


class UserRole(models.Model):
    pass


class Grade(models.Model):
    pass
