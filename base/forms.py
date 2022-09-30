# from dataclasses import fields
from django.forms import ModelForm  #ModelForm in built in form/ provides form
from .models import Room

#Naming convention is like ModelName-Form
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'  #this will create form based on data/metadata/fields of Room model
                            #we can add fields like ['host','topic','name']