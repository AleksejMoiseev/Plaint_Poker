from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic.edit import CreateView
from poker.forms import RegisterUserForm
from django.urls import reverse_lazy


# Create your views here.


def test(request):
    return HttpResponse('<h1 style="color: red; background: green">hello world</h1>')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    extra_context = {'title': 'Register'}
    success_url = reverse_lazy('/test/')

