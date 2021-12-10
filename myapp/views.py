from django.shortcuts import render
from rest_framework import viewsets

from .serializers import passengerSerializer
from .models import passenger
from .detectobject import a_test_file, process_image

# Create your views here.
from django.http import HttpResponse
import uuid
  
def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")  

import datetime  
# Create your views here.  
from django.http import HttpResponse, HttpResponseNotFound

#importing loading from django template  
from django.template import loader 

def index(request):  
    template = loader.get_template('index.html') # getting our template 
    name = {  
        'student':'rahul'  
    }   
    return HttpResponse(template.render(name))       # rendering the template in HttpResponse

from django.views.decorators.http import require_http_methods  
@require_http_methods(["GET"])  
def show(request):  
    return HttpResponse('<h1>This is Http GET request.</h1>')

@require_http_methods(["POST"])
def add_scanobject(request):
    print(request.POST)
    return render(request, "index.html")

@require_http_methods(["GET"])
def process_image_function(request):
    uuidfilename = uuid.uuid4().hex
    query = request.GET.get('myvalue')
    passval = "D:/Lambton documents/Sem 2 project/luggageproject/myapp/static/testimages/" + query
    process_image(passval, uuidfilename)
    #functionreturn = a_test_file()
    return HttpResponse(uuidfilename)

class passengerViewSet(viewsets.ModelViewSet):
    queryset = passenger.objects.all().order_by('passenger_name')
    serializer_class = passengerSerializer