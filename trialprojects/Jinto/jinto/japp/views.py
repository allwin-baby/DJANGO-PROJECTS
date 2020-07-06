from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from  rest_framework.parsers import JSONParser
from .models import Jinto
from .serializers import JintoSerializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.



@csrf_exempt
def jinto_list(request):
    if request.method  ==  'GET':
        jinto = Jinto.objects.last()
        serializer = JintoSerializers(jinto) 
        a = Jinto(link = "") 
        a.save()
        return JsonResponse(serializer.data,safe = False)   
    if request.method  ==  'POST':
        jinto = Jinto.objects.all()
        jinto.delete()
        data  = JSONParser().parse(request)
        serializer = JintoSerializers(data =data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status = 400 ) 