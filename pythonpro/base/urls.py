from django.urls import path
from pythonpro.base.views import home
from django.shortcuts import render

app_name = 'base'


def home(request):
    return render(request, 'base/home.html')


urlpatterns = [
    path('', home, name='home'),


]
