from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from  rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializers
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
#-------------------------------------------
@csrf_exempt
def article_list(request):
    if request.method  ==  'GET':
        article = Article.objects.all()
        serializer = ArticleSerializers(article,many = True) # becuse it is a queryset  (no!! because it returns multiple objects)
        #article = Article.objects.get(id =1) then 
        #serializer = ArticleSerializers(article ) ---> no 'many' parametre!!!
        return JsonResponse(serializer.data,safe = False) 
    elif request.method == 'POST':
        data  = JSONParser().parse(request)
        serializer = ArticleSerializers(data =data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)
        return JsonResponse(serializer.errors,status = 400 ) 
#-------------------------------------------
 
# POST ---> http://127.0.0.1:8000/  last / mukyam bigile
#  {
#   "id": 1,     -----------------> id is auto asssingend no effect code
#   "author": "allwin",
#   "title": "Django",
#   "email": "email"
# } 


#-------------------------------------------
@csrf_exempt
def article_detail(request,pk):
    try:
        article = Article.objects.get(pk = pk)
    except Article.DoesNotExist:
        return HttpResponse(status =404)
    if request.method == 'GET':
        serializer = ArticleSerializers(article,many = False) # only one object son many is flase
        return JsonResponse(serializer.data,safe = False) 
    elif request.method == 'POST':                #update operation
        data  = JSONParser().parse(request)
        serializer = ArticleSerializers(article,data = data)  #why added article ??? specify object and change only given firlds in data??
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status = 400 )
    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)  

#-------------------------------------------


# POST ---> http://127.0.0.1:8000/detail/2  -->last / mukyam bigile
#  {
#   "id": 1,     -----------------> id is auto asssingend no effect code
#   "author": "allwin",
#   "title": "Django",
#   "email": "email"
# } 
 
