from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
@login_required(login_url= 'acounts_index')
def index(request):
    if request.user.is_authenticated:
        user_id= request.user.id
        user_data= User.objects.get(id=user_id)
       
        context={'form':user_data}
   # return HttpResponse(f"hi is my {user_id}shop index")
    return render(request,'shop/shop_index.html',context)

