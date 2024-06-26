from django.shortcuts import render
from about_us.models import User
from django.views import View

# Create your views here.

def aboutUs(request):
    title = "ABOUT"
    return render(request, "about/about.html", context={"title" : title.capitalize()})
    
def users(request):
    title = "Users"
    users = User.objects.all()
    return render(request, "about/users.html", {"users" : users, "title": title})
    
# --------- This is a example of class based View in Djange ------------
class ClassBasedViewsExample(View): 
    def get(self, request):
        return render(request, 'about/class_view.html', {"title": "ClassView"})

    