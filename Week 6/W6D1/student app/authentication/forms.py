from pyexpat import model
from django.contrib.auth.models import User #it is not necessary to import User here, but it is a good practice
from django.contrib.auth.forms import UserCreationForm # it is not necessary to import UserCreationForm here, but it is a good practice


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username']