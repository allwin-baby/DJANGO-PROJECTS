
from django.urls import path
from .views import jinto_list

urlpatterns = [
    path('link/',jinto_list)
]