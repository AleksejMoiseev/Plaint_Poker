from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from poker import models as pm
from poker.forms import CustomUserChangeForm, CustomUserCreationForm


@admin.register(pm.User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username')
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = pm.User


@admin.register(pm.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'grade')


@admin.register(pm.VoteResult)
class VoteResultAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'grade')


@admin.register(pm.Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'properties')


@admin.register(pm.UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'role')
