from django.contrib import admin
from poker import models as em


@admin.register(em.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = '__all__'


@admin.register(em.VoteResult)
class VoteResultAdmin(admin.ModelAdmin):
    list_display = '__all__'


@admin.register(em.Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = '__all__'


@admin.register(em.UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = '__all__'
