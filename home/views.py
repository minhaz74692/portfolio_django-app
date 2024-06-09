from django.shortcuts import render


# Create your views here.
def home(request):
    title = 'Home'
    return render(request, 'home/home.html', context={"title":title})