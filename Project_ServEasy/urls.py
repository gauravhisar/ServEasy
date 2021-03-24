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
from Home.views import electricians, home
from Auth.views import login_page
from Home.views import home
from Auth.views import customer_login, customer_login_verification, customer_logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"), #returns dry Home page
    path('verified/<cid>/', home, name="verified_home"),  # returns home page for the corresponding customer
    path('customer_login/',customer_login , name="customer_login"), # returns login page
    path('customer_login_verification/',customer_login_verification , name="customer_login_verification"), # redirects to Home Page if login is verified otherwise same page will be rendered again
    path('logout/',customer_logout , name="customer_logout"), # redirects to dry Home page
    path('customer_signup/',customer_logout , name="customer_signup"),
    path('electricians', electricians ,name="electricians"),
]
