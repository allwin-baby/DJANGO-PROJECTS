from django.shortcuts import render
from django.views.generic import ListView,DetailView
from . import models

# Create your views here.


class QuestionListView(ListView):
    model = models.Question
class QuestionDetailView(DetailView):
    model = models.Question
    template_name = "quiz/quiz.html"
    context_object_name  = 'questions'
    
    def get_context_data(self,**kwargs):
        context = super.get_context_data(**kwargs)
        context['option_list'] = models.Option.objects.all()
        return context 



