from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	raise ValueError()
	return HttpResponse('<html><body>Ola Django</body></html>', content_type='text/html')