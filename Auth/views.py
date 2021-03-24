from django.shortcuts import render,redirect,reverse
from Home.views import home
from Auth.models import Customer

# Create your views here.
loggedin_userid = None
def customer_login(request, *args, **kwargs): # when we want to login this page will be displayed
	return render(request, "login.html", {"welcome1": "", "welcome2": "Customer Login"})

def customer_login_verification(request): # when someone enters details and press SIGNIN, we will return these pages depending upon whether the information is correct or not
	email = request.POST["mail"]
	pwd = request.POST["pwd"]
	try:
		mycustomer = Customer.objects.get(email = email)
	except : 
		return render(request, 'login.html', {'welcome1': 'Incorrect Email.', 'welcome2': 'Customer Login'})
	if mycustomer.pwd != pwd:
		return render(request, 'login.html', {'welcome1': 'Incorrect Password', 'welcome2': 'Customer Login'})
	else:
		global loggedin_userid
		loggedin_userid = mycustomer.cid
		print("I inside the login function")
		mycustomer.loggedin = 1
		mycustomer.save()
		return redirect(home, cid = mycustomer.cid)
# def customer_login_verification(request):
	# return home(request)

def customer_logout(request,*args, **kwargs ):
	global loggedin_userid
	mycustomer = Customer.objects.get(cid = loggedin_userid)
	loggedin_userid = None
	mycustomer.loggedin = 0
	mycustomer.save()
	return redirect(home)
	