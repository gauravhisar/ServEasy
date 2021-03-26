"""Project_ServEasy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home.views import  bookings,verify_booking,service_details #, electricians, carpenters, salonForMen, plumbers, BeauticiansForWomen,
#from Auth.views import login_page
from Home.views import home
from Auth.views import customer_login, customer_login_verification,customer_signup_verification, customer_logout, customer_signup


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"), #returns dry Home page
    path('verified/<cid>/', home, name="verified_home"),  # returns home page for the corresponding customer
   
    # Authentication Pages
    path('customer_login/',customer_login , name="customer_login"), # returns login page
    path('customer_login_verification/',customer_login_verification , name="customer_login_verification"), # redirects to Home Page if login is verified otherwise same page will be rendered again
    path('customer_signup/',customer_signup , name="customer_signup"), # returns signup page
    path('customer_signup_verification/',customer_signup_verification , name="customer_signup_verification"), # redirects to Home Page after verifying signup page, otherwise renders signup ppage again
    path('logout/<cid>/',customer_logout , name="customer_logout"), # redirects to dry Home page

    # Services  (5)   
    path('services/<servicename>/', service_details ,name="service"),
    path('verified/<cid>/services/<servicename>/', service_details, name="service"),
    
    # Service booking of customer
    path('verifybooking/<servicename>', verify_booking, name = "verify_booking"),# its is of no use, added this so that we donot get error
    path('verified/<cid>/verifybooking/<servicename>/', verify_booking, name = "verify_booking"), # redirects to booking page

    #Displaying Bookings of Customer
    # path('bookings/', bookings ,name="bookings"),   
    path('verified/<cid>/bookings/', bookings, name="bookings"), # returns booking page
    

]
