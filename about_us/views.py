from django.shortcuts import render
from about_us.models import User

# Create your views here.

def aboutUs(request):
    title = "ABOUT"
    return render(request, "about/about.html", context={"title" : title.capitalize()})
    
def users(request):
    title = "Users"
    users = User.objects.all()
    return render(request, "about/users.html", {"users" : users, "title": title})
    
    