from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name = 'acounts_index'),
    path('registeruser', views.registeruser,name = 'registeruser'),
    path('loginuser', views.loginuser,name = 'loginuser'),
    path('logoutuser', views.logoutuser,name = 'logoutuser'),
    path('changepassword', views.changepassword,name = 'changepassword'),

]
