from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import Enum
import uuid

from django.urls import reverse


class DateTimeFieldMixin:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class User(AbstractUser):
    pass


class Role(Enum):
    observer = 'observer'
    moderator = 'moderator'
    player = 'player'


class Task(models.Model, DateTimeFieldMixin):
    class STATUS:
        CREATED = 'created'
        IN_PROGRESS = 'in_progress'
        DONE = 'done'

        CHOICES = (
            (CREATED, 'created'),
            (IN_PROGRESS, 'in_progress'),
            (DONE, 'done')
        )

    name = models.CharField(max_length=150)
    url = models.URLField()
    status = models.SmallIntegerField(choices=STATUS.CHOICES, default=STATUS.CREATED)
    grade = models.IntegerField(null=True)
    room = models.ForeignKey(
        to='Room',
        on_delete=models.CASCADE,
        related_name='tasks',
        related_query_name='tasks_query'
    )


    def __repr__(self):
        return f"Task {self.pk} name {self.name} status {self.status}"


class VoteResult(models.Model):
    task = models.ForeignKey(to='Task', on_delete=models.CASCADE, related_name='vote_result')
    user = models.ForeignKey(to='User', on_delete=models.CASCADE, related_name='vote_user')
    grade = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Task: {self.task} User: {self.user}, Grade: {self.grade}"


class Room(models.Model):
    id = models.UUIDField(verbose_name='Room', editable=False, default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=50)
    properties = models.JSONField(null=False)

    def __repr__(self):
        return 'name room {}'.format(self.name)

    def get_absolut_url(self):
        name_path = '#'
        return reverse(name_path, kwargs={'id': self.pk})


class UserRole(models.Model):
    class STATUS:
        observer = Role.observer.name
        moderator = Role.moderator.name
        player = Role.player.name

        CHOICES = (
            (observer, Role.observer.name),
            (moderator, Role.moderator.name),
            (player, Role.player.name)
        )

    user = models.ForeignKey(to='User', on_delete=models.CASCADE, related_name='user_role')
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE, related_name='rooms')
    role = models.CharField(default=STATUS.player, choices=STATUS.CHOICES, max_length=50)

    class Meta:
        unique_together = ['user', 'room', 'role']

    def __repr__(self):
        return f"User: {self.user}  Role:{self.role} Room: {self.room}"
