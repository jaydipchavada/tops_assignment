from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def login(request):
    return render(request,'myapp/login.html')

def home(request):
    return render(request,'myapp/index.html')