from django.urls import path
from pythonpro.aperitivos.views import video
from django.shortcuts import render

app_name = 'aperitivos'

# def video(request):
#     return render(request, 'aperitivos/video.html')


urlpatterns = [
    path('<slug:slug>', video, name='video'),

]