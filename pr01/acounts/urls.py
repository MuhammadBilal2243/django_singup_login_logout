from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name = 'index'),
    path('registeruser', views.registeruser,name = 'registeruser'),
    path('loginuser', views.loginuser,name = 'loginuser'),
    path('logoutuser', views.logoutuser,name = 'logoutuser'),

]
