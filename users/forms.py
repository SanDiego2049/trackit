from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import login, authenticate

class LoginForm(AuthenticationForm):
    email = forms.EmailField(label='Enter Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    def confirm_login_allowed(self, user):
        if user.is_staff and not user.is_superuser:
            raise ValidationError(
                ("This account is not allowed here."),
                code='not_allowed',
            )
# class SignUpForm(UserCreationForm):
#     email= forms.EmailField()
#     first_name= forms.CharField()
#     last_name= forms.CharField()
#     date_of_birth = forms.DateTimeField()
#     class Meta:
#         model = User
#         fields= [ "first_name","last_name","username", "date_of_birth", "email", "password1", "password2"]
