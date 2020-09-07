from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
  
# Create your views here. 
def process_image_view(request): 

    processImage.objects.all().delete()
 
    if request.method == 'POST': 
        form = ProcessForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('palette') 
    else: 
        form = ProcessForm() 
    return render(request, 'upload.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfully uploaded') 

def home(request):
	return render(request, 'index.html',) 

def about(request):
	return render(request, 'about.html',) 

def examples(request):
	return render(request, 'examples.html',) 

def display_palette(request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of palette. 
        Palettes = processImage.objects.all()  
        return render(request, 'display_palette.html', {'palette' : Palettes}) 

