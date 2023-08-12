from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home (request):
    return render(request,"myapp/index.html")

def login(request):
    if request.POST:
        print("submit button hit")
        p_email = request.POST['Email']
        p_password = request.POST['password']
        print("====>email",p_email)
        uid = user.objects.get(email = p_email)
        print("=====>uid object",uid)
        if uid.password == p_password:
            if uid.role == "chairman":
                cid = chairman.objects.get(user_id = uid)
                print("chairman ==>",cid)
            else:
                pass
        else:
            print("==>invaild password")    
    else:
        print("only page refresh")
    return render(request,"myapp/login.html")