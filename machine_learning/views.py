from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def machineLearning(request):
    count = 5
    count+=1
    for i in range (1, 100):
        count+=i
    offering = {"count": count, "title":"Machine Learning", "developer":"Minhazul Islam", "nameList": ["Minhaz", "Monir", "Kamrul", "Mainul"]}
    return render(request, "ml/ml.html", context = offering)

def mlDescription(request):
    return render(request, "ml/description.html")

def random(request):
    return render(request, "ml/random.html")

def kNearest(request):
    return render(request, "ml/kn.html")

def dTree(request):
    return render(request, "ml/dtree.html")