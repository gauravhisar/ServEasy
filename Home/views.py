#https://www.toptal.com/django/django-top-10-mistakes
from django.shortcuts import render

# Create your views here.
def home(request, *args, **kwargs):
	return render(request, "index.html", {})

def electricians(request, *args, **kwargs):
	return render(request, "elec.html", {})

