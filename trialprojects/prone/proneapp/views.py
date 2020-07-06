from django.shortcuts import render
from django.http import HttpResponse
import requests
from . import forms
import http.client
from django.views.generic import View 
from rest_framework.views import APIView 
from rest_framework.response import Response 
from django.http import JsonResponse
import json
# Create your views here.
price=[]

def index(request):
    data={'riya':'RIYA IS A ERANAM KETTAVAL'}
    return render(request,'index.html',context=data)   # context is data'  but data written is  {{riya}} "" {{data.riya}}"" wont work


def form(request):
    if request.method == 'POST':
        data={'aftersubmit': "YOUR FORM SUBMITTED"}
        return render(request,'form.html',context=data) 
   
    key1="b043d96ed0mshcc4d47d4677e9fcp1204c7jsn3820d0bd3f4d"
    key2="62b40822dfmsh91d921fc3d73a82p189fa5jsnb7c994e5d70b" 
    key3="0f597f6809msh8463abefd5b750bp18b300jsn820a0dd37385"
    key4="7168bb7daamshd8174fabc2140c0p188e76jsn8f50ece7892b"
    url="https://www.flipkart.com/knotyy-flip-cover-realme-c3/p/itmc320f97933f3b?pid=ACCFZZK5HZUS79TX&lid=LSTACCFZZK5HZUS79TXTISZE8&marketplace=FLIPKART&srno=b_1_1&otracker=nmenu_sub_Electronics_0_Mobile%20Cases&fm=neo%2Fmerchandising&iid=en_myCwVpVOiGofIGECLAJK3%2BNwp4VWzI7tqxabgGcz80FJyZJqXtReHwDefb%2BDWzLC3d4XwgGQNpeoavlq4gatxA%3D%3D&ppt=browse&ppn=browse&ssid=5f2uuhn3y80000001592291695363"     
    conn = http.client.HTTPSConnection("price-history-charts.p.rapidapi.com")
    payload = ""
    headers = {
    'x-rapidapi-host': "price-history-charts.p.rapidapi.com",
    'x-rapidapi-key': key4,
    'content-type': "application/x-www-form-urlencoded"
    }
    conn.request("POST", "/ProductHistory?product_url="+url, payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data)

    #response = requests.get("https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple")
    #print(response.content)
    #quiz= response.json()
    #print(type(quiz))

    data={'form':forms.InputForm ,'beforesubmit':"yes"}            # template---->>>> {{form}} 
    return render(request,'form.html',context=data)   

    #data=forms.InputForm
    #return render(request,'form.html',{"form":data})     # template---->>>> {{form}}


from json import dumps 
def send_dictionary(request): 
    # create data dictionary 
    dataDictionary = { 
        'hello': 'World', 
        'geeks': 'forgeeks', 
        'ABC': 123, 
        456: 'abc', 
        14000605: 1, 
        'list': ['geeks', 4, 'geeks'], 
        'dictionary': {'you': 'can', 'send': 'anything', 3: 1} 
    } 
    # dump data 
    dataJSON = dumps(dataDictionary) 
    return render(request, 'landing.html', {'data': dataJSON}) 


class Chart(View): 
    def get(self, request, *args, **kwargs): 
        return render(request, 'chart.html') 

class ChartData(APIView): 
    authentication_classes = [] 
    permission_classes = [] 
   
    def get(self, request, format = None): 
        labels = [ 
            'January', 
            'February',  
            'March',  
            'April',  
            'May',  
            'June',  
            'July'
            ] 
        chartLabel = "my data"
        chartdata = [0, 10, 5, 2, 20, 30, 45] 
        data ={ 
                     "labels":labels, 
                     "chartLabel":chartLabel, 
                     "chartdata":chartdata, 
             } 
        return Response(data) 


