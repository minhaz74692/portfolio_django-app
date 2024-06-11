from django.urls import path
from . import views

urlpatterns = [
    path("", views.aboutUs, name =  'about'),
    path("users/", views.users , name = "users")
]