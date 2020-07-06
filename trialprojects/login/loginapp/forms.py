from django import forms
from django.contrib.auth.models import User  #User is in models.py
#from loginapp  import models # thettu
from loginapp.models import UserInfo
# we are creatin model forms forms that connect to models ,
# previously did that form created with 
# some fields and passsed to view as form(contxt)

class UserForm(forms.ModelForm):
    #additional fields other than in the  built in model User
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model=User
        fields=('username','email','password')  #why 2 passwords (maybe hashed password)

class UserInfoForm(forms.ModelForm):    # model name is UserInfo so UserInfoForm (mandatory)
#creating a form having 
#fields in the "UserInfo" model with selected fields as pic and url
    class Meta():
        model=UserInfo
        fields=('pic','urlfield')              


""" class UserInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)  #instead of extending from django default user class we are using a one to one relation ship to "userinfo" 
    #addition fields
    #TypeError: __init__() missing 1 required positional argument: 'on_delete'   hurray i corrected it
    urlfield = models.URLField(blank=True)
    pic = models.ImageField(upload_to='uploded_pics',blank=True) # stored in media/uploded_pics
    def __str__(self):    
        return self.user.username """