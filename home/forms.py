from django import forms
from django.forms import fields
from models import SignUp

class Signupform(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['name','email','contact','password','country','role']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        for instance in SignUp.objects.all():
            if instance.email == email:
                raise forms.ValidationError('email already present')
        return email
