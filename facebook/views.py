from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from facebook.models import profiler

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        context={
            "users_list": profiler.objects.all()
        }
    else:
        key=request.user.username
        try:
            context={
                "acc_box": profiler.objects.get(user_id=key),
                "users_list": profiler.objects.exclude(user_id=key).all()
                }
        except profiler.DoesNotExist:
            context={
                "user_det": profiler.objects.get(user_id="dummy"),
                "users_list": profiler.objects.all()
                }
    
    return render(request,"facebook/index.html",context)

def sign_in(request):
    if not request.user.is_authenticated:
        return render(request, "facebook/login.html")
    else: 
        key=request.user.username
        try:
            context={
            "user": request.user,
            "user_det":profiler.objects.get(user_id=key)
            }
        except profiler.DoesNotExist:
            context={
                "user_det": profiler.objects.get(user_id="dummy")
            }
        return render(request, "facebook/profile.html", context);

def login_acc(request):
    username=request.POST["username"]
    password=request.POST["password"]
    user=authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("signin"))
    else:
        return render(request, "facebook/login.html", {"message": "invalid credentials"})

def logout_acc(request):
    logout(request)
    # return HttpResponse("none")
    return render(request, "facebook/login.html", {"message": "Logged out"})

def online(request):
    if not request.user.is_authenticated:
        return HttpResponse("logout")
    else:
        return HttpResponse("login")

def signup(request):
    return render(request, "facebook/signup.html") 

def create_acc(request):
    name=request.POST["fullname"]
    username=request.POST["username"]
    email=request.POST["email"]
    password1=request.POST["password_one"]
    password2=request.POST["password_two"]
    date=str(request.POST["dob"])
    bio=request.POST["bio"]
    dp=request.POST["profile_url"]
    
    user=authenticate(request, username=username, password=password1)
    if user is not None:
        return render(request, "signup.html",{"message": "user already exist"})
    else:
            if password1==password2:
                new=User.objects.create_user(username,email,password1)
                new.save()
                info=profiler(user_id=username,name=name,email=email,bio=bio,profile_url=dp,dob=date)
                info.save()
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request,"signup.html",{"message": "Password does'nt match"})
    
def visit(request,user_id):
    try:
        check=profiler.objects.get(id=user_id)

    except:
        raise Http404("Does not Exist")

    context={
        "user_det":check
        } 
    return render(request,"facebook/visit.html",context)