from django.shortcuts import render
import datetime

def index(request):
    return render(request,template_name='index.html')
# Create your views here.

def blog(request,blog_id):
    return render(request,template_name='blog.html')

def test(request):
    return render(request,template_name='test.html')


def addblog(request):
    return render(request, template_name='add_blog.html')
