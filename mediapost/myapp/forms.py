from django import forms
from . models import MyPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MyPostForm(forms.ModelForm):
    class Meta:
        model = MyPost
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        # here we are using tuple because we are using build-in models
        fields = ('username', 'email', 'password1', 'password2')