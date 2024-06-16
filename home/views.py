from django.shortcuts import render
from . forms import RegistrationForms


# Create your views here.
def home(request):
    title = 'Home'
    return render(request, 'home/home.html', context={"title":title})

def userRegistration(request):
    title = "Sign Up"
    if request.method == "POST":
        regForm = RegistrationForms(request.POST)
        # print(regForm)
        if regForm.is_valid():
            print("This is post statement")
            print(regForm.cleaned_data['password'])
            print(regForm.cleaned_data['repassword'])

    else:
        regForm = RegistrationForms()
        print("this is get statement")
        
    # regForm.order_fields(field_order=['last_name' , 'email ' , 'first_name' ,'password',])
    return render(request, "home/registration.html", context= {"forms": regForm, "title": title})