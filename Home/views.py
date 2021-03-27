#https://www.toptal.com/django/django-top-10-mistakes
import random
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from Home.models import *
from django.template import loader
from django.db import connection
from datetime import date,datetime

# Create your views here.

# Home Page View
def home(request, *args, **kwargs):

		# No keyword argument means the person is not loggedin
		if len(kwargs) == 0:  
			return render(request, "index.html", {"loggedin": False})
		else:

			try: 
				mycustomer = Customer.objects.get(cid = kwargs['cid']) 
			except: 
				# if someone makes direct request to a cid which do not exist
				return redirect(home) 

			if not mycustomer.loggedin: # if the person is logged in db 
				return redirect(home)

			return render(request, "index.html", {"loggedin": kwargs['cid'], "user": mycustomer.c_name})


# showing details of the requested service
def service_details(request, *args, **kwargs):

	services_available = {'electricians': 'elec.html', 'carpenters' : 'carp.html', 'salonForMen':'salonForMen.html', 'plumbers': 'plumbers.html', 'BeauticiansForWomen' : 'beauticiansForWomen.html'}
	for servicename in services_available.keys():
		if kwargs['servicename'] == servicename:
			break
	else: 
		return HttpResponseNotFound('<h1>Page not found</h1>')

	# getting all the sub-services in that servicename
	service_req  = Service.objects.filter(category__exact = service_to_category[servicename])

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

# to show all the bookings customer has made in past
def bookings(request, *args, **kwargs):

	# fetching data from DB for the particular customer
	with connection.cursor() as cursor:
		mycustomer = Customer.objects.get(cid = kwargs['cid'])
		cursor.execute("select distinct(b.bid), time(b.bdate), b.status, b.category, s.dscrptn, sp.sp_name, date(b.bdate), b.amount from booking b, service s, bookedfor a, serviceprovider sp where b.bid=a.bid and a.sid=s.sid and b.cid=%s and b.spid=sp.spid",[mycustomer.cid])
		row = cursor.fetchall()
		objects = []

	#list of objects of class event 
	for i in range(len(row)):
		objects.append(Booking())

	# storing all the data in ojects of booking class
	for i in range(len(row)):
		objects[i].bid=row[i][0]
		objects[i].timing=row[i][1]
		objects[i].status = codetostatus[row[i][2]]
		objects[i].category = category_to_service[row[i][3]]
		objects[i].dscrptn = row[i][4]
		objects[i].sp_name = row[i][5]
		objects[i].bdate = row[i][6]
		objects[i].amount = row[i][7]

	# sorting all the records in their date and time order
	objects.sort(key=lambda a:a.timing, reverse=True)
	objects.sort(key=lambda a:a.bdate, reverse=True)

	return render(request,'bookings.html',{"loggedin": kwargs['cid'], "user":mycustomer.c_name, "records":objects })

# service booking 
def verify_booking(request, *args, **kwargs):
	if len(request.POST) == 1: #no services selected
		return redirect(service_details, cid = kwargs['cid'], servicename = kwargs['servicename'] )

	
	bcategory = service_to_category[kwargs['servicename']]
	bdate = date.today()
	btime = datetime.now().strftime("%H%M")   # service will be available with half hour
	bstatus = 'B'
	bcustomer = Customer.objects.get(cid = kwargs['cid'])
	bservices = list(dict(request.POST).values())

 	#deleting csrf token as we donot need it right now
	bservices.pop(0)

	assigned_sp = Serviceprovider.objects.filter(category__exact = bcategory)
	assigned_sp = assigned_sp[random.randint(0,len(assigned_sp)-1)]
	bservices = [int(x[0]) for x in bservices]
	
	# find total amount
	amount = 0
	req_services = []  # in Service Object Format used in creating bookedfor objects
	for i in bservices:
		req_services.append(Service.objects.get(sid = i))
		amount += req_services[-1].price
		
	# creating a booking and saving it in DB	
	new_booking = Booking(cid = bcustomer,spid = assigned_sp, timing = btime, category = bcategory, status = bstatus, amount = amount)
	new_booking.save()

	# saving all the sub-services customer has booked
	for s in req_services:
		Bookedfor(bid = new_booking, sid = s).save()
	
	return redirect(bookings, cid = kwargs['cid']) # redirecting customer to bookings page

