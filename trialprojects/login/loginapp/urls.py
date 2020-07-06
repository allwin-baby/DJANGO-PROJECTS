#from django.conf.urls import url
#url vs path???
from django.urls import path
from loginapp import views  #from . import views

# app_name='loginapp' 

# ---->called name space WASTED MT 1 1/2 hr 
# ERROR: Django - Reverse for '' not found. '' is not a valid view function or pattern name


urlpatterns = [
    path('',views.homeView,name="homeUrl"),
    path('register/',views.registerView,name="registerUrl"),      # YAAAAAAAA      #{{% url 'registerView' %}}
    path('login/',views.loginView,name='loginUrl'),
    path('logout/',views.logoutView,name='logoutUrl'),
    path('special/',views.special,name='specialUrl'),
] 
