from django.urls import path
from . import views

urlpatterns=[
    path("<int:question_id>/",views.details),
    path("<int:question_id>/result",views.result),
    path("vote/<int:question_id>",views.vote),
    path("",views.index,name="polls"),
    path("setting",views.setting,name="setting"),
    path("contact",views.contact,name="contact"),
]