from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home (request):
    if "Email" in request.session:
        return render(request,"myapp/index.html")
    else:
        return render(request,"myapp/login.html")

def login(request):
      if "Email" in request.session:
           uid = user.objects.get(email = request.session['Email'])
           if uid.role == "chairman":
               cid = chairman.objects.get(user_id = uid)
               context={
                        "cid": cid,
                        "uid": uid,
                    }
               return render(request,"myapp/index.html",context) 
           else:
               pass                      
      elif request.POST:
        print("submit button hit")
        p_email = request.POST['Email']
        p_password = request.POST['password']
        print("====>email",p_email)
        try:
            uid = user.objects.get(email = p_email)
            print("=====>uid object",uid)
            if uid.password == p_password:
                if uid.role == "chairman":
                    cid = chairman.objects.get(user_id = uid)
                    request.session['Email'] = uid.email
                    print(cid)
                    context={
                        "cid": cid,
                        "uid": uid,
                    }
                    return render(request,"myapp/index.html",context)
                else:
                    pass
            else:
                print("==>invaild password")
                context = {
                    "e_msg" : "Invalid Password "
                }
                return render(request,"myapp/login.html",context)
        except:
            context = {
                    "e_msg" : "Invalid email or password  "
                }
            return render(request,"myapp/login.html",context)


      else:
        print("only page refresh")
        return render(request,"myapp/index.html")

def logout(request):
    if 'Email' in request.session:
        del request.session['Email']
        return render(request,"myapp/login.html")
    else:
        return render(request,"myapp/login.html")
    
def profile(request):
    if 'Email' in request.session:
         uid = user.objects.get(email = request.session['Email'])
         if uid.role == "chairman":
               cid = chairman.objects.get(user_id = uid)
               context={
                        "cid": cid,
                        "uid": uid,
                    }
               return render(request,"myapp/profile.html",context) 
         

def change_password(request):
    if 'Email' in request.session:
        uid = user.objects.get(email=request.session['Email'])
        if uid.role == "chairman":
            cid = chairman.objects.get(user_id=uid)
            current_password = request.POST['current_password']
            new_password = request.POST['new_password']
            if uid.password == current_password:
                uid.password = new_password  
                uid.save()  # Save the changes 

                context = {
                    "cid": cid,
                    "uid": uid,
                }
                return render(request, "myapp/profile.html", context)
            else:
                e_msg = "Invalid current password"
                del request.session['Email']  
                context = {
                    'e_msg': e_msg
                }
                return render(request, "myapp/login.html", context)
        else:
            context = {
                "cid": cid,  
                "uid": uid,
            }
            return render(request, "myapp/profile.html", context)
    
def update_chairman_profile(request):
     if 'Email' in request.session:
        uid = user.objects.get(email=request.session['Email'])
        if uid.role == "chairman":
            cid = chairman.objects.get(user_id=uid)

            cid.first_name = request.POST['first_name']
            cid.last_name = request.POST['last_name']
            cid.contect_no = request.POST['contect_no']

            if "pic" in request.FILES:
                cid.pic = request.FILES['pic']
                #cid.save()
                

            cid.save() #update

            context = {

                    "uid" : uid,
                    "cid" : cid,
                }

            return render(request, "myapp/profile.html", context)
           
def add_notice(request):
     if 'Email' in request.session:
           uid = user.objects.get(email=request.session['Email'])
           if uid.role == "chairman":
                cid = chairman.objects.get(user_id=uid)
                if request.POST:
                    nid = Notice.objects.create(notice_title = request.POST['Notice_title'],notice_description = request.POST['Notice_description'])

                    if "pic" in request.FILES and "video" in request.FILES:
                        nid = Notice.objects.create(notice_title = request.POST['Notice_title'],notice_description = request.POST['Notice_description'],pic = request.FILES['pic'],video = request.FILES['video'])

                    elif "pic" in request.FILES:
                        nid = Notice.objects.create(notice_title = request.POST['Notice_title'],notice_description = request.POST['Notice_description'],pic = request.FILES['pic'])

                    elif "video" in request.FILES:
                        nid = Notice.objects.create(notice_title = request.POST['Notice_title'],notice_description = request.POST['Notice_description'],video = request.FILES['video'])

                    context = {

                        "uid" : uid,
                        "cid" : cid,
                        }

                    return render(request, "myapp/add-notice.html", context)
                else:
                    context = {

                        "uid" : uid,
                        "cid" : cid,
                        }

                    return render(request, "myapp/add-notice.html", context)
                

    
    

