from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def machineLearning(request):
    return HttpResponse('This is machine learning page')