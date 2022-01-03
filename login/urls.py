from django.urls import path
from . import views

urlpatterns =[
    path('users/', views.moi),
    path("route/", views.appjson),
]