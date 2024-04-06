from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

# Create your views here.
def home(request):
    #all()
    data = Student.objects.all()
    data1 = data.values()
    #print(data)
    return HttpResponse(data1)
    #return HttpResponse(data)
