from django.urls import path
from . import views

urlpatterns=[
    path("index",views.index,name="polls"),
    path("setting",views.setting,name="setting"),
    path("contact",views.contact,name="contact"),
]