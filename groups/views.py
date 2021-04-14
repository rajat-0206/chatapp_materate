from django.shortcuts import render,redirect,Http404,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib.auth.hashers import check_password,make_password,check_password
from .models import *


def login_user(request):
    if(request.user.is_authenticated):
        return redirect("/")
    if request.method=='POST':
        username= request.POST['username']
        password=request.POST['password']

        user= authenticate(request,username=username,password=password)
        if (user and str(user)!="admin"):
                login(request,user)
                return redirect('/')
        else:
            error1="invalid login details supplied!"
            return render(request,'login.html',{'error':error1})
    else:
        return render(request,"login.html")


def home(request):
    if(request.user.is_authenticated==True):
        user = request.user.username
        try:
            groupid = request.GET["room"]
            userobj = User.objects.get(username=user)
            group = room.objects.filter(members=userobj)
            current = room.objects.get(id=groupid)
            listofmembers = current.members.all()
            if(userobj not  in listofmembers):
                raise Http404
            else:
                msg = message.objects.filter(group_id=groupid)
                return render(request,"index.html",{"user":userobj,"rooms":group,"messages":msg,"current":current})
        except:
            userobj = User.objects.get(username=user)
            group = room.objects.filter(members=userobj)
            msg = message.objects.filter(group=group[0])
            return render(request,"index.html",{"user":userobj,"rooms":group,"messages":msg,"current":group[0]})
    else:
        return redirect("/login")


def send(request):
    if(request.method=="POST"):
        try:
            text = request.POST["message"]
            user = request.POST["user"]
            group = request.POST["room"]
        except:
            return HttpResponse("Some values are missing")
        try:
            reply = request.POST["reply"]
            temp = message.objects.get(id=reply)
            print(temp.text)
            msg = message.objects.create(group_id=group,sender_id=user,text=text,reply=temp)
        except:
            msg = message.objects.create(group_id=group,sender_id=user,text=text)
        
        return HttpResponse("Message added")


def logout_user(request):
    logout(request)
    request.session['loged'] = False
    request.session['uesrname'] =""
    return redirect('/')