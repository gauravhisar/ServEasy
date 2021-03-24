#https://www.toptal.com/django/django-top-10-mistakes
from django.shortcuts import render
from Auth.models import Customer, loggedin_userid
from Home.models import Booking

# Create your views here.
def home(request, *args, **kwargs): # {'cid': 45}  WRITE IN TRY EXCEPT FORM 
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
		if len(kwargs) == 0: 
			return render(request, "elec.html", {"loggedin": False})
		else:
			try: 
				mycustomer = Customer.objects.get(cid = kwargs['cid'])
			except: 
				return render(request, "elec.html", {"loggedin": False})

			if not mycustomer.loggedin:
				return render(request, "elec.html", {"loggedin": False})

			return render(request, "elec.html", {"loggedin": kwargs['cid'], "user": mycustomer.c_name})

def carpenters(request, *args, **kwargs):
		if len(kwargs) == 0: 
			return render(request, "carp.html", {"loggedin": False})
		else:
			try: 
				mycustomer = Customer.objects.get(cid = kwargs['cid'])
			except: 
				return render(request, "carp.html", {"loggedin": False})

			if not mycustomer.loggedin:
				return render(request, "carp.html", {"loggedin": False})

			return render(request, "salonForMen.html", {"loggedin": kwargs['cid'], "user": mycustomer.c_name})

def salonForMen(request, *args, **kwargs):
		if len(kwargs) == 0: 
			return render(request, "salonForMen.html", {"loggedin": False})
		else:
			try: 
				mycustomer = Customer.objects.get(cid = kwargs['cid'])
			except: 
				return render(request, "salonForMen.html", {"loggedin": False})

			if not mycustomer.loggedin:
				return render(request, "salonForMen.html", {"loggedin": False})

			return render(request, "salonForMen.html", {"loggedin": kwargs['cid'], "user": mycustomer.c_name})

def plumbers(request, *args, **kwargs):
		if len(kwargs) == 0: 
			return render(request, "plumbers.html", {"loggedin": False})
		else:
			try: 
				mycustomer = Customer.objects.get(cid = kwargs['cid'])
			except: 
				return render(request, "plumbers.html", {"loggedin": False})

			if not mycustomer.loggedin:
				return render(request, "plumbers.html", {"loggedin": False})

			return render(request, "plumbers.html", {"loggedin": kwargs['cid'], "user": mycustomer.c_name})

def BeauticiansForWomen(request, *args, **kwargs):
		if len(kwargs) == 0: 
			return render(request, "beauticiansForWomen.html", {"loggedin": False})
		else:
			try: 
				mycustomer = Customer.objects.get(cid = kwargs['cid'])
			except: 
				return render(request, "beauticiansForWomen.html", {"loggedin": False})

			if not mycustomer.loggedin:
				return render(request, "beauticiansForWomen.html", {"loggedin": False})

			return render(request, "beauticiansForWomen.html", {"loggedin": kwargs['cid'], "user": mycustomer.c_name})

def bookings(request):
	#mycustomer = Customer.objects.get(cid = kwargs['cid'])
	myBookings=Booking.objects.all()
	bnum={"bookin_number":myBookings}
	return render(request, "bookings.html", bnum)