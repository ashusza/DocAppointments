from django.shortcuts import render ,redirect
from django.contrib.auth.models import User   #hashing 
from django.contrib.auth import logout, login ,authenticate
from django.views import View
from django.contrib import auth
from django.contrib import messages
from app_Patients.models import Patient
from django.db.models import Count #dashbord ko kamm auxa 
from django.middleware.csrf import get_token as csrf

# Create your views here.
class logoutview (View):
    def get (self,request):
        logout (request)
        
class loginview (View):
    def get(self,request):
        return render(request, 'accounts/login.html', {'csrf_token': csrf(request)})

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        user = authenticate ( request ,username = username,password = password,email=email)

        if user is not None:
            if email:
                user.email = email
                user.save()
            login(request,user)
            messages.success(request,"Login successfully")
            return render(request,'doctors/doctor_home.html')
            
        else:
            messages.error (request,"Login Fail")
        return redirect ('login')

class RegisterView(View):
    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username, email=email, password=password)
        if user is not None:
            user.first_name = fname
            user.last_name = lname
            user.is_active = True
            user.save()
            
            return redirect('login')
        return redirect('register')




        
        
