from django.shortcuts import render
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
    if request.method == 'POST':
        private_phrase = request.POST['private_phrase']
        
        assign = Phrase(private_phrase=private_phrase)
        assign.save()
        messages.success(request,'Cleanup Successfull')
    
    return render(request,'index.html')