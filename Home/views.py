#https://www.toptal.com/django/django-top-10-mistakes
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from Auth.models import Customer, loggedin_userid
from Home.models import Service, service_to_category
# Create your views here.
def home(request, *args, **kwargs): # {'cid': 45}  
		if len(kwargs) == 0: 
			return render(request, "index.html", {"loggedin": False})
		else:
			try: 
				mycustomer = Customer.objects.get(cid = kwargs['cid'])
			except: 
				return redirect(home)
				# return render(request, "index.html", {"loggedin": False})

			if not mycustomer.loggedin:
				return redirect(home)

			return render(request, "index.html", {"loggedin": kwargs['cid'], "user": mycustomer.c_name})


def service_details(request, *args, **kwargs):
	services_available = {'electricians': 'elec.html', 'carpenters' : 'carp.html', 'salonForMen':'salonForMen.html', 'plumbers': 'plumbers.html', 'BeauticiansForWomen' : 'beauticiansForWomen.html'}
	for servicename in services_available.keys():
		if kwargs['servicename'] == servicename:
			break
	else: 
		return HttpResponseNotFound('<h1>Page not found</h1>')

	service_req  = Service.objects.filter(category__exact = service_to_category[servicename])
	print(service_req[0])

	if len(kwargs) == 1: # in kwargs, there is only service name
		return render(request, services_available[servicename], {"loggedin": False, "service_req": service_req})
	
	else:      #there is both servicename and cid
		try: 
			mycustomer = Customer.objects.get(cid = kwargs['cid'])
		except:  # incase the requested cid doesnt exist 
			return redirect(service_details, servicename = services_available[servicename])

		if not mycustomer.loggedin: # cid exists but the person is not logged in
			return redirect(request, servicename = services_available[servicename])

		return render(request, services_available[servicename], {"loggedin": kwargs['cid'], "user": mycustomer.c_name, "service_req": service_req, 'servicename': servicename})

def bookings(request, *args, **kwargs):
	try:
		mycustomer = Customer.objects.get(cid = kwargs['cid'])
	except :
		return redirect(home)
	return render(request, "bookings.html", {"loggedin": kwargs['cid'], "user":mycustomer.c_name})

def verify_booking(request, *args, **kwargs):
	l = []
	for i in request.POST:
		l.append([i, request.POST[i]])
	return HttpResponse(str(l))
def booking_done(request, *args, **kwargs): #redirects tp home page only
	pass

