from django.urls import path
from graphviz import view
from . import views
url_patterns =[
    
    path("",views.index,name="index"),
    path("<str:name>",views.greeting,name="greeting")
]