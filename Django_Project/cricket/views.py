from django.shortcuts import render
from .models import Destination
# Create your views here.

def cricket(request):
    destinations = Destination.objects.all()   
    return render(request,'index.html',{'destinations':destinations})