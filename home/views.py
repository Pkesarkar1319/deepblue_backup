from home import mongodb
from attrs import validators
from django.contrib.auth import models
from django.shortcuts import render,HttpResponse
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from pydantic import validate_arguments
from home.models import SignUp
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
import random
import json
import os
from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from home.models import SignUp
from home.models import ResumeFile
#from django.contrib.auth.models import Signup
#from .models import PreRegistration

from django.contrib.auth import login,logout,authenticate

from resumeparser.settings import EMAIL_HOST_USER, EMAIL_USE_TLS
# Create your views here.
signup = SignUp.empAuth_objects

def mainpage(request):
    if request.method == 'POST':
          email=request.POST.get('email')
          password=request.POST.get('password')
          print(email,password)
          if(SignUp.empAuth_objects.all().filter(email=email,password=password,role="Recruiter").exists()):
          
                  return render(request, 'base1.html')
          else:
                if(SignUp.empAuth_objects.all().filter(email=email,password=password,role="Candidate").exists()):   
                  return render(request, 'main_page.html')
                
          
                else:
                    if(SignUp.empAuth_objects.all().filter(email=email,password=password,role="Admin").exists()):   
                        return render(request, 'base1.html')
                    else:

                        # Return a 'disabled account' error message
                        return render(request,'index.html')
          
def index(request):
    return render(request, 'index.html')
def editprofile(request):
    return render(request, 'editprofile.html')
def landingpage(request):
    return render(request, 'landingpage.html')
def signup(request):
    return render(request, 'signup.html')
def database(request):
    skills=mongodb.get_skills()

    print(skills)
    return render(request,'database.html',{'skillset':json.dumps(skills)})
    
    
    
def upload(request):
    
    return render(request,'base1.html')
    
def demoupload(request):
    return render(request, 'demoupload.html')

def forgetpassword(request):
    return render(request, 'forget_password.html')



def creatingOTP():
    otp = ""
    for i in range(4):
        otp+= f'{random.randint(1,9)}'
    return otp

def sendEmail(email):
    otp = creatingOTP()
    send_mail(
    'One Time Password',
    f'Your OTP pin is {otp}',
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
    )
    return otp

def registration(request):
    global em,na,pas,cont,rol,count,context
    if request.method=="POST":
         #global email
         em=request.POST.get('email')
         na=request.POST.get('name')
        # email=request.POST.get('name')
         pas=request.POST.get('password')
         cont=request.POST.get('phone')
         count=request.POST.get('country')
         rol=request.POST.get('role')
         #otp=sendEmail(email)
         context={
             
             "email": em,
             
             
         }
         if(SignUp.empAuth_objects.all().filter(email=em).exists()):   
                  return render(request, 'index.html')
         else:

         
            return render(request, 'otp_verify.html',context)



def upload_resume(request):
    if request.method=="POST":
        file=request.FILES.getlist('file')

        
        #_, file = request.FILES.popitem()  # get first element of the uploaded files
        print(file)
        #suff_list = ['pdf','doc','docx','html','txt']
        #file = file[0]  # get the file from MultiValueDict
        for f in file:
            r= ResumeFile(file=f)
            #if(ResumeFile.empAuth_objects1.all().filter(file.validate_arguments=email,password=password,role="Admin").exists()):
            s = str(f)
            if (s.endswith(('pdf','doc','docx','html','txt'))):
                r.save()

            

               
            

        return render(request,"database.html")
def otp_success(request):
   s = SignUp(email=em,name=na,password=pas,contact=cont,country=count,role=rol)
   s.save()
   return render(request, 'index.html',context)
    
def userside(request):
    return render(request,'index.html')

def re_load(request):
    return render(request, 'otp_verify.html',context)

def forget(request):
    global forget_email
    if request.method=="POST":
         #global email
         forget_email=request.POST.get('email')
         
         context={
             
             "email": forget_email,
             
             
         }
         
         if(SignUp.empAuth_objects.all().filter(email=forget_email).exists()):   
                  return render(request, 'otp_verify1.html',context)
        
         else:
                  return render(request, "index.html")

def forget1(request):
    print ("hello")
    if request.method == 'POST':
        em=request.POST.get('email')

         
        context={
             
             "email": em,
             
             
         }
          
        password=request.POST.get('password')
        s = SignUp.empAuth_objects.filter(email=forget_email).update(password = password)
        return render(request, 'index.html')