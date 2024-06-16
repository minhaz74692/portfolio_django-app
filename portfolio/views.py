from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def portfolio(request):
    title = 'portfolio'
    return render(request, "portfolio/portfolio.html", context={"title":title})

def signup(request):
    title = "Sign Up"

    if request.method == "POST":
        fm = UserCreationForm()
        try:
             fm.save()
        except:
            print('User sign up failed')

        if fm.is_valid():
            print('User created')
            fm.save()

    else:
        fm = UserCreationForm()

    return render(request, 'portfolio/signup.html', {"form": fm, "title": title})

