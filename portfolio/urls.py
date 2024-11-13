from django.urls import path
from . import views

urlpatterns =[

    path("", views.portfolio, name  = "portfolio"),
    path("signup/", views.signup, name  = "signup"),
    
    # changes 3
]