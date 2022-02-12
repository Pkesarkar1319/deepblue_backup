from pyrsistent import v
from home import mongodb
from attrs import validators
from django.contrib.auth import models
from django.shortcuts import render,HttpResponse
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
#from pydantic import validate_arguments
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
from pprint import pprint
#from django.contrib.auth.models import Signup
#from .models import PreRegistration

from django.contrib.auth import login,logout,authenticate

from resumeparser.settings import EMAIL_HOST_USER, EMAIL_USE_TLS
# Create your views here.
signup = SignUp.empAuth_objects
filterdata={}

def filter(request):
    mandatory_filed=[]
    optional_filed=[]
    exp=[]
    partial=[]
    complete=[]
    notmatch=[]
    global filterdata
   # print(mandatory_filed)
    filterdata={}
    if request.method=='POST':
        skills=request.POST.get('myInput')
        loc=request.POST.get('loc')
        lang=request.POST.get('lang')
        r1=int(request.POST.get('myRange'))
        r2=int(request.POST.get('myRange1'))
        check=request.POST.get('mandatory')
        
        s=skills.split(",")
        l=loc.split(",")
        la=lang.split(",")
        c=check.split(",")
        opt=list(set(s)-set(c))
        exp.append(r1)
        exp.append(r2)


        mandatory_filed.append(c)
        mandatory_filed.append(exp)

        optional_filed.append(opt)
        #optional_filed.append(l)
        optional_filed.append(la)

        

        

        
        print("*****Mandatory",mandatory_filed)
        print("*****optional",optional_filed)
        results=mongodb.search(mandatory_filed,optional_filed)
        print(len(results))
        for i in results:
        # print("mandate value:{} optional value:{}".format(i['mandatory_value'],i['optional_value']))
         if (i['mandatory_value'] > 0 and i['matched_mandatory_skills'] != []):
            if (i['mandatory_value'] == 1):
                complete.append(i)
            else:
                partial.append(i)


         else:
            notmatch.append(i)

        complete.sort(key=lambda e:(e['optional_value']),reverse=True)
        partial.sort(key=lambda e:(e['mandatory_value'],e['optional_value']),reverse=True)
        notmatch.sort(key=lambda e:(e['optional_value']),reverse=True)
        pprint(partial)
        pprint(complete)
        pprint(notmatch)
        print("partial len",len(partial))
        print("complete len",len(complete))
        print("notmatch len",len(notmatch))
        
        
        filterdata['complete']=complete
        filterdata['partial']=partial
        filterdata['notmatched']=notmatch
        filterdata['skillset']=mongodb.get_skills()
    return render(request,'complete.html',filterdata)
        
def complete(request):
    return render(request,'complete.html',filterdata)
def partial(request):
    return render(request,'partial.html',filterdata)
def notmatched(request):
    return render(request,'notmatched.html',filterdata)


       
       
      


    

def mainpage(request):
    if request.method == 'POST':
          email=request.POST.get('email')
          password=request.POST.get('password')
          print(email,password)
          if(SignUp.empAuth_objects.all().filter(email=email,password=password,role="Recruiter").exists()):
          
                  return render(request, 'base1.html')
          else:
                if(SignUp.empAuth_objects.all().filter(email=email,password=password,role="Candidate").exists()):   
                  return render(request, 'candidate.html')
                
          
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
    
    context={}
    context['skillset']=mongodb.get_skills()
    
    return render(request,'database.html',context)
    
    
    
def upload(request):
    
    return render(request,'base1.html')
    
def demoupload(request):
    return render(request, 'demoupload.html')

def forgetpassword(request):
    return render(request, 'forget_password.html')




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

def candidate(request):
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