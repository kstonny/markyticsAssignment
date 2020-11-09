from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, logout,login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib import messages
from .models import Reportform 
from .forms import ReportFor 
# Create your views here.

def signup(request):
    print("signup running")
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        password1 = request.POST["password1"]
        email = request.POST["email"]

        user = User.objects.create_user(username=username, password=password1, email=email)
        user.save()
        print("user created")
        return redirect("index")   

    else:
        return render(request, 'signup.html')

# def report_submit(request):
    
#     else:
#         return render(request, 'signup.html')



def login_view(request):

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username = username, password = password)
        print("got it")
        if user is not None:
            auth.login(request, user)
            print("valid credentials")
            messages.error(request,"")
            
           # return render(request, 'login.html')
            return redirect("index")
            
        else:
            messages.error(request,"Invalid Username/Password")
            print("invalid credentials")
            return render(request, "login.html")

    else:
        print("really") 
        return render(request, "login.html")
        

def home_view(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def user_logout(request):
    logout(request)
    return redirect('index')

def report_incident(request):
    class Meta:
        model = report_incident
    if request.method == 'POST':
        location_1 = request.POST["location_1"]
        location_2 = request.POST["location_2"]
        time = request.POST["time"]
        severity = request.POST["severity"]
        discription = request.POST["discription"]
        casue = request.POST["casue"]
        action = request.POST["action"]
        submitted = request.POST.get("submitted", False)
        reported_by = request.POST["reported_by"]
        date = request.POST["date"]
        type_env = request.POST.get("type_env", False)
        type_inj = request.POST.get("type_inj", False)
        type_prop = request.POST.get("type_prop", False)

        if type_env == 'on':
            type_env = True
        else:
            type_env = False
        
        if type_prop == 'on':
            type_prop = True
        else:
            type_prop = False
        
        if type_inj == 'on':
            type_inj = True
        else:
            type_inj = False

        if submitted == 'on':
            submitted = True
        else:
            submitted = False

        report = Reportform.objects.create(location_1=location_1, location_2=location_2, casue=casue, time=time, severity=severity, discription=discription,  action=action, submitted=submitted, reported_by=reported_by, date=date, type_env=type_env, type_inj=type_inj, type_prop=type_prop)
        

        report.save()
        context = { 
        "saved_message" : "Report Saved",
    } 
        print("report created")
        
        return render(request, "report_incident.html", context) 
    
    else:
        context = { 
        "saved_message" : "",
        } 
        return render(request, "report_incident.html", context)   
        
