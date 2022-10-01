from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# models are just database tables representation
# class name is a table name
# each variable/field of that class will be columns of that table

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

#Room is subclass of Topic 
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic= models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)  #null true menas description field can be null, and blank true menas decription field can be empty
    participants = models.ManyToManyField(User, related_name='participants', blank=True )
    updated = models.DateTimeField(auto_now=True)   #auto_now takes snapshot of field every time it is updated
    created = models.DateTimeField(auto_now_add=True) #auto_now_add takes snapshot of field when it first time created.
    
    class Meta:
        ordering = ['-updated', '-created'] # updated, created will be in ascending order while -updated, -created will be descending
                    #first item of this list is prioratise and it'll will chain down
    
   
        
    def __str__(self):
        return self.name
    
#create a class or model called Message
class Message(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)   # we are creating one-to-maney relationship between Room and Message, Messgae is child of Room, so if a Room is deleted then all child messages will be deleted ,we used CASCADE for that
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)   #auto_now takes snapshot of field every time it is updated
    created = models.DateTimeField(auto_now_add=True) #auto_now_add takes snapshot of field when it first time created.
    
    def __str__(self):
        return self.body[0:50]