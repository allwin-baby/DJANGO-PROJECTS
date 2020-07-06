from django.shortcuts import render
import requests
from django.views.generic import View , TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView,
from django.http import HttpResponse
from . import models # from same directory  impoert models.py

def homeView(request):
    return render(request,'index.html')
class CBV(View):
    def get(self,request):
        return HttpResponse('CLASS BASED VIEW')

class TemplateBasedView(TemplateView):  #class base temlate view with simple context dict
    template_name = "templateView.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme']  = 'BASIC INJECTION'    # Only important line
        return context
    


class SchoolListView(ListView):
    template_name = 'cbvapp/schoollist.html'    
     #    <------only needed for inapp templates--------> {% extends "cbvapp/base.html" %}
    model = models.School                       #------->School become school_list
    # school_list
    #  <ol>
    #     {{ for school in school_list }}          ----->
    #     <h2><li>{{ school.name }}</li></h2 >             
    #     {% endfor %}
    # </ol>

# class SchoolListViewBySpecifingContextname(ListView):
#     model = models.School    
#     context_object_name = 'schools'
#     school_list
#     <ol>
#        {{ for school in schools }}          ----->  school_list become schools
#        <h2><li>{{ school.name }}</li></h2 >             
#       {% endfor %}
#     </ol>

class SchoolDetailView(DetailView):   #saves a lot of time like  object.all....
    model = models.School           
    template_name = "cbvapp/school.html"    #inapp template
    context_object_name = 'school_detail'  #------- id you dont specify  automatically 

  
    #takes same as models name and add nothing(like did it in List view as add _list)
#    <h2>NAME : {{ school_detail.name}}</h2>
#    <h2>LOCATIOIN : {{school_detail.location}}</h2>
#    </div>
#    {% for students in school_detail.students.all  %}
#    <p>NAME :{{ students.name }}</p>
#    <p> AGE: {{ students.age}}</p>
#    {% endfor %}

class StudentListView(ListView):
    model = models.Student
    template_name=  'cbvapp/sudentlist.html'
    #context_object_name = 'students'

class SchoolCreateView(CreateView):
    model = models.School      #no nedd to set template the default template = school_form.html
    fields = ('name','location',)     # comma is imp  , #fields that allowed to edit      # you can change name but not place( if you want then add to field)

class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name',)