#https://www.toptal.com/django/django-top-10-mistakes
from django.shortcuts import render
from Auth.models import Customer, loggedin_userid

# Create your views here.
def home(request, *args, **kwargs): # {'cid': 45}
		if len(kwargs) == 0: 
			return render(request, "index.html", {"loggedin": False})
		else:
			try: 
				mycustomer = Customer.objects.get(cid = kwargs['cid'])
			except: 
				return render(request, "index.html", {"loggedin": False})

			if not mycustomer.loggedin:
				return render(request, "index.html", {"loggedin": False})

			return render(request, "index.html", {"loggedin": kwargs['cid'], "user": mycustomer.c_name})


def electricians(request, *args, **kwargs):
	return render(request, "elec.html", {})

