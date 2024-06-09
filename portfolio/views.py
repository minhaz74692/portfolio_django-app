from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def portfolio(request):
    title = 'portfolio'
    return render(request, "portfolio/portfolio.html", context={"title":title})