from django.shortcuts import render,redirect
from .models import User
# Create your views here.
def index(request):
    return render(request,"user_app/index.html")
def register(request):
    if request.method == "POST":
        user1={
        'fname':request.POST['name'],
        'lname':request.POST['alias'],
        'email':request.POST['email'],
        'password':request.POST['Password'],
        'cpassword':request.POST['cpassword'],
        }
        user=User.objects.validate(user1)
        if 'error' in user:
            print user['error']
            context={
                'errors':user['error']
            }
            return render(request,"user_app/index.html",context)
        else:
            context={
            'msg':"you have successfully registered",
            'user':user
            }
        return render(request,"user_app/index.html",context)
    # else:
    #     return redirect('/')
def login(request):
    if request.method == "POST":

        user=User.objects.login(request.POST)
        # print type(user)
        if 'error' in user:
            print user['error']
            context={
                'errors':user['error']
            }
            return render(request,"user_app/index.html",context)
        else:

            request.session['name']=user['user'].name
            request.session['userid']=user['user'].id
        return redirect("belt:index")
