from django.shortcuts import render,redirect,reverse
from Home.views import home
from Home.models import Customer

# Create your views here.

# Displays Login Page
def customer_login(request, *args, **kwargs): 
	return render(request, "login.html", {"welcome1": "", "welcome2": "Customer Login", 'welcome3': ''})


# Displays SignUp page
def customer_signup(request, *args, **kwargs): 
	return render(request, "signup.html", {"welcome1": "", "welcome2": "New Customer ?"})


# Login Verification 
def customer_login_verification(request): 
	email = request.POST["mail"]
	pwd = request.POST["pwd"]

	# Email should Match
	try:
		mycustomer = Customer.objects.get(email = email)
	# Otherwise show error message
	except : 
		return render(request, 'login.html', {'welcome1': 'Incorrect Email.', 'welcome2': 'Customer Login', 'welcome3': 'New User? Please signup first!'})
	
	# Password should be correct
	if mycustomer.pwd != pwd:
		return render(request, 'login.html', {'welcome1': 'Incorrect Password', 'welcome2': 'Customer Login', 'welcome3': ''})
	# If it is correct, login the person and direct to home page
	else:
		mycustomer.loggedin = 1
		mycustomer.save()
		return redirect(home, cid = mycustomer.cid)


# Signup Verification and adding a user
def customer_signup_verification(request): 
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

	# also check that email should not exist in DB
	try: 
		mycustomer = Customer.objects.get(email = email)
		return render(request, "signup.html", { "welcome1": "Email Already Exists", "welcome2": "New Customer ?"})
	
	except : # At last, store user in the DB
		mycustomer = Customer(email = email, pwd = pwd, address = address, contact_no = phn, c_name = names, loggedin = 1)
		mycustomer.save()
		return redirect(home, cid = mycustomer.cid)


# Logout 
def customer_logout(request,*args, **kwargs ):
	mycustomer = Customer.objects.get(cid = kwargs['cid'])
	mycustomer.loggedin = 0
	mycustomer.save()
	return redirect(home)
	