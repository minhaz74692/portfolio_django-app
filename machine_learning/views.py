from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def machineLearning(request):
    count = 5
    count+=1
    for i in range (1, 100):
        count+=i
    offering = {"count": count, "title":"Machine Learning", "developer":"Minhazul Islam", "nameList": ["Minhaz", "Monir", "Kamrul", "Mainul"]}
    return render(request, "machine_learning/ml.html", context = offering)

def mlDescription(request):
    title = "Description"
    return render(request, "machine_learning/description.html", context={"title": title,})

def random(request):
    return render(request, "machine_learning/random.html")

def kNearest(request):
    return render(request, "machine_learning/kn.html")

def dTree(request):
    count = 23
    title = "Decission Tree"
    return render(request, "machine_learning/dtree.html", context={'c':count, "title": title})

def learning(request):
    title = "Learning"
    return render(request, "machine_learning/learning.html", context={"title": title})