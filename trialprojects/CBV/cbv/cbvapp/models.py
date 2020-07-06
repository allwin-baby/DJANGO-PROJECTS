from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 256)
    location = models.CharField(max_length= 256)

    def __str__(self):
        return self.name 
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('cbvapp:detail', kwargs={'pk': self.pk})

class Student(models.Model):   #Field 'id' expected a number but got 'students'. ????
    name = models.CharField(max_length=256)
    age= models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name = 'students',on_delete= models.CASCADE) #related name is used when detail of  {% for students in school_detail.students.all  %}
    
    def __str__(self):
        return self.name

 



    
