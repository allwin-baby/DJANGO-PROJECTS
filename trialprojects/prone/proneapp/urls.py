from django.conf.urls import url
from  proneapp import views

urlpatterns = [
    url(r'^$',views.index,name='index'),    # why url not path             
    url(r'^form/',views.form,name='form'),
    url('chart/', views.Chart.as_view()), 
    url('api/', views.ChartData.as_view()),
    url(r'^json/',views.send_dictionary,name='send_dictionary')
]