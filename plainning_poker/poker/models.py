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
    task = models.ForeignKey(to='Task', on_delete=models.CASCADE)
    user = models.ForeignKey(to='User', on_delete=models.CASCADE, related_name='vote_user')
    grade = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Room(models.Model):
    id = models.UUIDField(verbose_name='Room', editable=False, default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=50)
    properties = models.JSONField(null=False)


class UserRole(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE, related_name='user_role')
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE, related_name='rooms')
    #role =

    class Meta:
        unique_together = ['user', 'room']


class Grade(models.Model):
    pass
