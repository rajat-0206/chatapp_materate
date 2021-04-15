from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class room(models.Model):
    id = models.AutoField(primary_key=True,editable=False,null=False)
    members = models.ManyToManyField(User)
    name = models.CharField(max_length=1000,null=False)

    def __str__(self):
        return self.name
    
    def get_members(self):
        members = self.members.all()
        result = []
        for i in members:
            result.append(i.first_name+" "+i.last_name)
        return ", ".join(i for i in result)

class message(models.Model):
     id = models.AutoField(primary_key=True,editable=False,null=False)
     group = models.ForeignKey("room", on_delete=models.CASCADE)
     sender = models.ForeignKey(User, on_delete=models.CASCADE)
     time = models.TimeField(auto_now_add=True)
     text = models.CharField(max_length=10000)
     reply = models.ForeignKey("message",null=True,blank=True,on_delete=models.CASCADE)

     def __str__(self):
         return self.text +" by "+self.sender.first_name+" in room "+self.group.name

    
def add_to_group(sender,instance,created,**kwargs):
    if(created==True):
        groups = room.objects.all()
        for i in groups:
            i.members.add(instance)

post_save.connect(add_to_group,sender=User)