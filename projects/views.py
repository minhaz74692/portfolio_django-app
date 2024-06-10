from django.shortcuts import render

# Create your views here.

def projects(request):
    title = "Projects"
    return render(request, "projects/projects.html", context={"title": title})

def flutter(request):
    title = "flutter"
    return render(request, "projects/flutter.html", context={"title": title})
