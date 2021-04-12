from django.shortcuts import render,redirect,Http404,HttpResponse
from .models import *

def home(request):
    user = request.GET["username"]
    try:
        groupid = request.GET["room"]
        userobj = User.objects.get(username=user)
        group = room.objects.filter(members=userobj)
        current = room.objects.get(id=groupid)
        msg = message.objects.filter(group_id=groupid)
        return render(request,"index.html",{"user":userobj,"rooms":group,"messages":msg,"current":current})
    except:
        pass
    userobj = User.objects.get(username=user)
    group = room.objects.filter(members=userobj)
    msg = message.objects.filter(group=group[0])
    return render(request,"index.html",{"user":userobj,"rooms":group,"messages":msg,"current":group[0]})

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