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