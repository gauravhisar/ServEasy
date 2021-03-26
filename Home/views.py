#https://www.toptal.com/django/django-top-10-mistakes
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from Auth.models import Customer, loggedin_userid
from Home.models import *
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import connection

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
		# return render(request, "bookings.html",{})
		# mycustomer = Customer.objects.get(cid = kwargs['cid'])
		# mybooking = Booking.objects.filter(cid = kwargs['cid'])
		# bookingxservice = Bookedfor.objects.filter(bid_id=mybooking[0].bid)
		# services = Service.objects.get(sid_id=bookingxservice.sid)
		# return render(request, "bookings.html", {"loggedin": kwargs['cid'], "user": mycustomer.c_name,"bid": mybooking[0].bid, "desc": services.dscrptn, "cat": mybooking[0].category, "timing": mybooking[0].timing, "status": mybooking[0].status})
		#myBookings=Booking.objects.get(cid=kwargs['cid'])
		#myBookings.entry_set.set([e1, e2])
		#return render(request, "bookings.html", {"loggedin": kwargs['cid'], "entry_set":[]})

		# bookings_list = Booking.objects.order_by('-pub_date')[:5]
		# context = {'Booking_list': Booking_list}
		# return render(request, 'bookings.html', context)

		# bookings_list = Booking.objects.all(cid=kwargs['cid'])
		# template = loader.get_template('bookings.html')
		# context = {
		# 	'bookings_list': bookings_list,
		# }
		# return HttpResponse(template.render(context, request))

		with connection.cursor() as cursor:
			mycustomer = Customer.objects.get(cid = kwargs['cid'])
			cursor.execute("select distinct(b.bid), time(b.bdate), b.status, b.category, s.dscrptn, sp.sp_name, date(b.bdate) from booking b, service s, bookedfor a, serviceprovider sp where b.bid=a.bid and a.sid=s.sid and b.cid=%s and b.spid=sp.spid",[mycustomer.cid])
			# cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
			row = cursor.fetchall()
			objects = []

		#list of objects of class event 
		for i in range(len(row)):
			objects.append(Booking())



		for i in range(len(row)):
			objects[i].bid=row[i][0]
			objects[i].timing=row[i][1]
			objects[i].status =row[i][2]
			objects[i].category = category_to_service[row[i][3]]
			objects[i].dscrptn = row[i][4]
			objects[i].sp_name = row[i][5]
			objects[i].bdate = row[i][6]
			#objects[i].cid = row[4]
			#objects[i].sspid=row[5]

		records=[]
		for i in range(len(objects)):
			records.append(objects[i])

		return render(request,'bookings.html',{"loggedin": kwargs['cid'], "user":mycustomer.c_name, "records":records })
		# return row
	# try:
	# 	mycustomer = Customer.objects.get(cid = kwargs['cid'])
	# except :
	# 	return redirect(home)
	# return render(request, "bookings.html", {"loggedin": kwargs['cid'], "user":mycustomer.c_name})

def verify_booking(request, *args, **kwargs):
	l = []
	for i in request.POST:
		l.append([i, request.POST[i]])
	return HttpResponse(str(l))
def booking_done(request, *args, **kwargs): #redirects tp home page only
	pass

