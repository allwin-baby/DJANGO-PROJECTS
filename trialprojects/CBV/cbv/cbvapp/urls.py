from django.conf.urls import url
from django.urls import path
from cbvapp import views

app_name = 'cbvapp'   # FOR URL TEMPLATE TAGGING
#<li><a class = "navbar-brand" href="{% url 'cbvapp:list' %}"></a></li>

urlpatterns = [
    path('',views.SchoolListView.as_view(),name = 'list'), 
    url(r'^(?P<pk>\d+)/$' ,views.SchoolDetailView.as_view(),name = 'detail'), #detail viewe is assossiated with pk
    #path('sl/', views.SchoolDetailView.as_view(),name = 'detail') didnt work
    #IMPPPPPPPP !!!!!!Generic detail view SchoolDetailView must be called with either an object pk or a slug in the URLconf.
    path('students/',views.SchoolListView.as_view(),name = 'stlist'),
    url(r'^create/$',views.SchoolCreateView.as_view(),name = 'create'),
    url(r'^update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(),name='update'),
   
]