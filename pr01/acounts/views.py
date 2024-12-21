from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterUserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

#imports for login
from .forms import LoginUserForm
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("shop_index")   
    return render(request,"acounts/index.html")
def registeruser(request):
    
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            username=request.POST["username"]
            password=request.POST["password1"]
            to_email=request.POST["email"]
            massage=f"YOUR acount name is {username}passord is  {password}."
            form.save()
            send_mail("WELCOME",f"YOUR acount name is {username}passord is  {password}.","bilal0302599@gmail.com",[to_email,],fail_silently=False,)

            return redirect("loginuser")
    else:
        form = RegisterUserForm()
    context={"form":form }
    return render(request,"acounts/registeruser.html" ,context)

@login_required(login_url= 'acounts_index')
def logoutuser(request):
    logout(request)
    return redirect("loginuser")


def loginuser(request):
 
    if request.method=='POST':
            
            username=request.POST["username"]
            password=request.POST["password"]
            
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("shop_index")
            else:
                return HttpResponse("invilid user name or password")
        
    else:
        form = LoginUserForm()
    
        
    context={"form":form}
    return render(request,"acounts/loginuser.html",context)
@login_required(login_url= 'acounts_index')
def changepassword(request):
    if request.method=='POST':
         p1=request.POST['password1']
         p2=request.POST['password2']
         if p1==p2:
                user_id= request.user.id
                user_data= User.objects.get(id=user_id)
                user_data.set_password(p1)
                user_data.save()
                return redirect("loginuser")    
    return render(request,'acounts/changepassword.html')
