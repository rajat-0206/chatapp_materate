from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="homepage"),
    path('login',views.login_user,name="login"),
    path('addmessage',views.send,name="send message"),
    path("logout",views.logout_user,name="logout")

]
