from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
class LoginUserForm(ModelForm):
    class Meta:
        model=User
        fields="__all__"


        