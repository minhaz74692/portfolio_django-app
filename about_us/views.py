from django.shortcuts import render

# Create your views here.

def aboutUs(request):
    title = "ABOUT"
    return render(request, "about/about.html", context={"title" : title.capitalize()})
    
    