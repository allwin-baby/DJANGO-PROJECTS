"""cbv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from cbvapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homeView,name = 'homeUrl'),
    path('cbv/',views.CBV.as_view()),
    path('tview/',views.TemplateBasedView.as_view()),
    path('cbvapp/',include('cbvapp.urls',namespace= 'cbvapp'))  #name space is used in template tagging  linke{% url 'cbvapp:index'%}
]
