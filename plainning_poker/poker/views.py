from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rest_framework import status

from poker.forms import RegisterUserForm


def test(request):
    return HttpResponse('<h1 style="color: red; background: green">hello world</h1>')


def pageNotFound(request, exception):
    return render(request=request, template_name='errors/error_404.html', status=status.HTTP_404_NOT_FOUND)


def unauthorized_error(request, exception):
    return render(request=request, template_name='errors/error_401.html', status=status.HTTP_401_UNAUTHORIZED)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'poker/register_test.html'
    extra_context = {'title': 'Register'}
    success_url = reverse_lazy('/test/')


