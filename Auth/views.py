from django.shortcuts import render,redirect,reverse
from Home.views import home
from Home.models import Customer

# Create your views here.
loggedin_userid = None # Not of any use, will remove it later
def customer_login(request, *args, **kwargs): # when we want to login this page will be displayed
	return render(request, "login.html", {"welcome1": "", "welcome2": "Customer Login", 'welcome3': ''})
def customer_signup(request, *args, **kwargs): # when we want to singup this page will be displayed
	# # Testing Code
	# try:
	# 	o = Customer.objects.get(email = "hello@gmail.com")
	# 	o.delete()
	# except :
	# 	pass
	return render(request, "signup.html", {"welcome1": "", "welcome2": "New Customer ?"})

def customer_login_verification(request): # when someone enters details and press SIGNIN, we will return these pages depending upon whether the information is correct or not
	email = request.POST["mail"]
	pwd = request.POST["pwd"]
	try:
		mycustomer = Customer.objects.get(email = email)
	except : 
		return render(request, 'login.html', {'welcome1': 'Incorrect Email.', 'welcome2': 'Customer Login', 'welcome3': 'New User? Please signup first!'})
	if mycustomer.pwd != pwd:
		return render(request, 'login.html', {'welcome1': 'Incorrect Password', 'welcome2': 'Customer Login', 'welcome3': ''})
	else:
		global loggedin_userid
		loggedin_userid = mycustomer.cid
		print("I inside the login function")
		mycustomer.loggedin = 1
		mycustomer.save()
		return redirect(home, cid = mycustomer.cid)

def customer_signup_verification(request): # when someone enters details and press SIGNIN, we will return these pages depending upon whether the information is correct or not
	names = request.POST['name']
	email= request.POST['mail']
	phn = request.POST['phn']
	pwd= request.POST['pwd']
	address = request.POST['address']
	e = ["" for i in range(5)]
	flag = 0
	if len(names) == 0:
		flag = 1
		e[0] = "Enter your name"

	if len(phn) < 10:
		flag = 1
		e[1] = "Enter valid phone number"

	if len(address) == 0:
		flag  =  1
		e[2]= "Enter address"

	if len(email) == 0:    
		flag = 1
		e[3] = "Enter Valid Email"

	if len(pwd) < 8:
		flag = 1
		e[4] = "Password should be greater than 8 characters"
	if flag == 1:
		return render(request, 'signup.html',
                      {'welcome1': '', 'welcome2': 'New Customer ?', 'e1': e[0], 'e2': e[1], 'e3': e[2], 'e4': e[3], 'e5': e[4]})

	try:
		mycustomer = Customer.objects.get(email = email)
		return render(request, "signup.html", { "welcome1": "Email Already Exists", "welcome2": "New Customer ?"})
	except : 
		mycustomer = Customer(email = email, pwd = pwd, address = address, contact_no = phn, c_name = names, loggedin = 1)
		mycustomer.save()
		return redirect(home, cid = mycustomer.cid)



def customer_logout(request,*args, **kwargs ):
	global loggedin_userid
	mycustomer = Customer.objects.get(cid = kwargs['cid'])
	loggedin_userid = None
	mycustomer.loggedin = 0
	mycustomer.save()
	return redirect(home)
	