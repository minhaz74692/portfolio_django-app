from django.urls import path
from . import views

urlpatterns =[

    path("", views.machineLearning),
    path("description/", views.mlDescription),
    path("random/", views.random),
    path("kn/", views.kNearest),
    path("d-tree/", views.dTree),
]