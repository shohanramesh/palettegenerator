# forms.py 
from django import forms 
from .models import *
  
class ProcessForm(forms.ModelForm): 
  
    class Meta: 
        model = processImage 
        fields = ['Choose_Image'] 