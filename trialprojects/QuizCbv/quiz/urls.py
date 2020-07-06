from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'quiz'

urlpatterns = [
    path('q/',views.QuestionListView.as_view(),name = 'question')    ,
    path('quiz/',views.QuestionDetailView.as_view(),name = 'quiz')
]