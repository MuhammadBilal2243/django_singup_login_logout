from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterUserForm
#imports for login
from .forms import LoginUserForm
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def index(request):
    return render(request,"acounts/index.html")
def registeruser(request):
    
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("for is submited")
            return HttpResponse("user is crated")
    else:
        form = RegisterUserForm()
    context={"form":form }
    return render(request,"acounts/registeruser.html" ,context)


def logoutuser(request):
    logout(request)
    return HttpResponse("you log out good its working")





def loginuser(request):
 
    if request.method=='POST':
            
            username=request.POST["username"]
            password=request.POST["password"]
            
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponse("congrates u login")
            else:
                return HttpResponse("invilid user name or password")
        
    else:
        form = LoginUserForm()
    
        
    context={"form":form}
    return render(request,"acounts/loginuser.html",context)
