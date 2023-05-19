from django.db import models  
from django.forms import fields ,ModelForm 
from .models import nuser,Image, suggestion ,startup,entrepreneur
from django import forms  
  
  
class nuserForm(forms.ModelForm):
    class Meta:
        model = nuser
        fields = '__all__'
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

class startupForm(forms.ModelForm):
    class Meta:
        model = startup
        fields = '__all__'

class suggestionForm(forms.ModelForm):
    class Meta:
        model = suggestion
        fields = '__all__'

class entrepreneurForm(forms.ModelForm):
    class Meta:
        model = entrepreneur
        fields = '__all__'