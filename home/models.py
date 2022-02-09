from django.db import models
from django.db.models.fields import EmailField
from django.core.validators import FileExtensionValidator
class SignUp_Manager(models.Manager):
    Email = ""
    Password = ""
    def __init__ (self,Email,Password):

        self.email = Email
        self.password = Password

    def get_queryset(self):
        
        return super().get_queryset().filter(email= "em" ,password= "paass")
class SignUp(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    contact = models.BigIntegerField()
    password = models.CharField(max_length=20) 
    country = models.CharField(max_length=30)
    
    role = models.CharField(max_length=10, default='Candidate')
    
    #def __str__(self):
     #   return self.email
    empAuth_objects = models.Manager()
    #signup = SignUp_Manager.Manager()
    



class ResumeFile(models.Model):
    #validators = [FileExtensionValidator( allowed_extensions= ["jpg"] ) ]
    id = models.AutoField(primary_key=True)
    file = models.FileField( upload_to = "")
    empAuth_objects1 = models.Manager()


    
    