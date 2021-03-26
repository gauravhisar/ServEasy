#https://www.toptal.com/django/django-top-10-mistakes
from django.shortcuts import render
from Auth.models import Customer, loggedin_userid
from Home.models import Booking, Serviceprovider, Bookedfor, Service, Customer
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import connection

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
			cursor.execute("select distinct(b.bid), b.timing, b.status, b.category, s.dscrptn from booking b, service s, bookedfor a where b.bid=a.bid and a.sid=s.sid and b.cid=%s",[mycustomer.cid])
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
			objects[i].category =row[i][3]
			objects[i].dscrptn = row[i][4]
			#objects[i].cid = row[4]
			#objects[i].sspid=row[5]

		records=[]
		for i in range(len(objects)):
			records.append(objects[i])

		return render(request,'bookings.html',{"loggedin": kwargs['cid'], "user":mycustomer.c_name, "records":records })
		# return row
