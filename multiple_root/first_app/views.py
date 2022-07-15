from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import User,AbstractUser
from.forms import Register_form,Login_form
# Create your views here.
def index(request):
    return render(request,'first_app/index.html')
def register_page(request):
    msg = None
    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('/login_page/')
        else:
            msg = 'form is not valid'
    else:
        form = Register_form()
    return render(request,'first_app/register.html',{'form':form,'msg':msg})
def login_page(request):
    msg = None
    if request.method == 'POST':
        form = Login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None and user.is_admin:
                login(request,user)
                return redirect('/admin_dashboard/')
            elif user is not None and user.is_staff:
                login(request,user)
                return redirect('/staff_dashboard/')
            elif user is not None and user.is_customer:
                login(request,user)
                return redirect('/customer_dashboard')
            else:
                msg = 'invalid credintial'
        else:
            msg = 'enter valid credintial'
        return render(request,'first_app/login.html',{'form':form,'msg':msg})
def home(request):
    return render(request,'first_app/home.html')

def Is_admin(request):
    return render(request,'first_app/admin_dashboard')
def Is_staff(request):
    return render(request,'first_app/staff_dashboard')
def Is_customer(request):
    return render(request,'first_app/customer_dashboard')