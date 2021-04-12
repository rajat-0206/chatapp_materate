from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="homepage"),
    path('addmessage',views.send,name="send message")
]
