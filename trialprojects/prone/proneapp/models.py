from django.db import models

# Create your models here.

class Question(models.Model):
    question=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return str(self.question)     #__str__ returned non-string
        
class Option(models.Model):
    question=models.ForeignKey('Question',on_delete=models.CASCADE)
    op1=models.CharField(max_length=100)
    op2=models.CharField(max_length=100)
    op3=models.CharField(max_length=100)

    def __str__(self):
        return str(self.question)  #__str__ returned non-string

class Answer(models.Model):
    question=models.ForeignKey('Question',on_delete=models.CASCADE)
    answer=models.CharField(max_length=100)

    def __str__(self):
        return str(self.answer)    #__str__ returned non-string