from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic.edit import CreateView
from poker.forms import RegisterUserForm
from django.urls import reverse_lazy
from django.shortcuts import render
from rest_framework import status


# Create your views here.


def test(request):
    return HttpResponse('<h1 style="color: red; background: green">hello world</h1>')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    extra_context = {'title': 'Register'}
    success_url = reverse_lazy('/test/')


def page_not_found(request, exceptions):
    render(request=request, template_name='error_404.html', status=status.HTTP_404_NOT_FOUND)


def unauthorized_error(request, exceptions):
    render(request=request, template_name='error_401.html', status=status.HTTP_401_UNAUTHORIZED)

