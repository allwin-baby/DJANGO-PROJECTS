from django.db import models
from django.contrib.auth.models import User  #default django user model with 
#username,password,email,lname,fname etc..
# Create your models here.


class UserInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)  #instead of extending from django default user class we are using a one to one relation ship to "userinfo" 
    #addition fields
    #TypeError: __init__() missing 1 required positional argument: 'on_delete'   hurray i corrected it
    urlfield = models.URLField(blank=True)
    pic = models.ImageField(upload_to='uploded_pics',blank=True) # stored in media/uploded_pics
    def __str__(self):    
        return self.user.username

