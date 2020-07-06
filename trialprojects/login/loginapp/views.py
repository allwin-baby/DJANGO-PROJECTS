from django.shortcuts import render
from loginapp import forms
from loginapp.forms import UserForm,UserInfoForm

from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse,HttpResponseRedirect
#from django.core.urlresolvers   import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def homeView(request):
    return render(request,"loginapp/home.html")

@login_required
def logoutView(request):
    logout(request)
    #return HttpResponse(request,'loginapp/home.html')  
    # !!! errror quote_from_bytes() expected bytes  what is the speciality  of HttpResponseRedirect(reverse('homeUrl'))
    return HttpResponseRedirect(reverse('homeUrl'))   # reversiing url pattern name to view.
@login_required
def special(request):
    return HttpResponse(request,'loginapp/home.html')


def registerView(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)     #creating an object of UserForm and passing post data 
        userinfo_form = UserInfoForm(data=request.POST)     #same
        if user_form.is_valid() and userinfo_form.is_valid() :
            user = user_form.save()  #object have method save to database
            user.set_password(user.password)  # set password hashes the user.password 
            user.save()  #after hashing saving with new password

            userinfo = userinfo_form.save(commit=False) #saving object of UserInforForm 
            userinfo.user=user #there is sa one to one relationship bw 
            userinfo.pic = request.FILES['pic']                               #Userinfo and user(userinfo contains a user)
            userinfo.save()
            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,userinfo_form.errors)    
    return render(request,'loginapp/register.html',{'user_form':forms.UserForm(),
                                                    'profile_form':forms.UserInfoForm(),
                                                    'registered':registered})
def loginView(request): #dont use login,logout etc because it is imported
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)

        user =authenticate(username=username,password= password) #simple 

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('homeUrl'))
            else:
                return HttpResponse("ACCOUNT IS  NOT ACTVE")
        else:
            print("FALIeD")
            return HttpResponse("invalid login credentials")

    return render(request,'loginapp/login.html',{}) 