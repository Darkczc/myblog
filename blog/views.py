from django.shortcuts import render
import datetime

def index(request):
    return render(request,template_name='index.html')
# Create your views here.
